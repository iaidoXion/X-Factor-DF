from datetime import timedelta, datetime
from pprint import pprint

import requests
from teradataml import *
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from common.menu import MenuSetting
from common.DB.jdbc import db_select, db_create, connect, history_select, database_traffic, user_traffic
import json
import math

menuListDB = MenuSetting()
connect_DBList = connect_DBList()


with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
Customer = SETTING['PROJECT']['CUSTOMER']
WorldUse = SETTING['PROJECT']['MAP']['World']
KoreaUse = SETTING['PROJECT']['MAP']['Korea']
AreaUse = SETTING['PROJECT']['MAP']['Area']['use']
AreaType = SETTING['PROJECT']['MAP']['Area']['type']
Login_Method = SETTING['PROJECT']['LOGIN']

def index(request):
    returnData = {'menuList': menuListDB}
    return render(request, 'web/index.html', returnData)

def dashboard(request):
    res_data = {}
    if not 'sessionid' in request.session:
        res_data['error'] = '먼저 로그인을 해주세요.'
        return render(request, 'common/login.html', res_data)
    else:
        dashboardType = 'dataFabric/webQuery_DF.html'
        returnData = {'menuList': menuListDB, 'Login_Method': Login_Method}
        return render(request, dashboardType, returnData)

def dataFabric_Settings(request):
    returnData = {'menuList': menuListDB, 'Customer': Customer,}
    return render(request, 'dataFabric/setting_DF.html', returnData)

############################ X-factor-DF ############################################
def dataFabric_webQuery(request):
    returnData = {'menuList': menuListDB, 'Customer': Customer}
    return render(request, 'dataFabric/webQuery_DF.html', returnData)

def dataFabric_monitoring(request):
    historyDB = history_select()
    db_trafficDB = database_traffic()
    user_trafficDB = user_traffic()
    returnData = {'menuList': menuListDB, 'Customer': Customer, 'history': historyDB, 'db_traffic' : db_trafficDB, 'user_traffic' : user_trafficDB}
    return render(request, 'dataFabric/monitoring_DF.html', returnData)

def dataFabric_navigator(request):
    TERADATA = False
    POSTGRES = False
    qry = """
        select UPPER(database_type) from xfactor.connect_tera  group by database_type;
    """
    qry2="""
        select * from xfactor.connect_tera where database_type = 'TERADATA';
    """
    column = db_select(qry)
    result = db_select(qry2)
    if result['status'] == 200 :
        result = result['data'].values.tolist()
    
    if column['status'] == 200 :
        column = column['data'].values.tolist()
        
    for i in column :
        if i == ['TERADATA'] :
            TERADATA = True
        elif i == ['POSTGRES'] :
            POSTGRES = True
    returnData = {'menuList': menuListDB, 
                  'Customer': Customer, 
                  'data' : result, 
                  "TERADATA" : TERADATA,
                  "POSTGRES" : POSTGRES}
    print()
    return render(request, 'dataFabric/navigator_DF.html', returnData)

def dataFabric_setting(request):
    returnData = {'menuList': menuListDB, 'Customer': Customer, 'connect_DBList': connect_DBList}
    return render(request, 'dataFabric/setting_DF.html', returnData)

#################################### api ############################################
@csrf_exempt
def dataFabric_api(request) :
    data = str(request.POST['data'])
    if data.lower().startswith('select') :
        result = db_select(data)
        
        if result['status'] == 200 :
            column = result['data'].columns.values.tolist()
            data = result['data'].values.tolist()
            returnData = {
                'status' : result['status'],
                'column' : column,
                'data' : data,
                'type' : result['type']
            }
        elif result['status'] == 400 :
            returnData = result
    elif data.lower().startswith('create') :
        result = db_create(data)
        
        if result['status'] == 200 :
            returnData = {
                'status' : result['status'],
                'data' : result['data'],
                'type' : result['type']
            }
        elif result['status'] == 400 :
            returnData = result
    return JsonResponse(returnData)

@csrf_exempt
def settings_api(request) :
    print('success')
    data = request.POST
    
    data_list ={
        'db' : data['db'],
        'db_name' : data['name'],
        'db_host' : data['host'],
        'db_port' : data['port'],
        'user_id' : data['id'],
        'user_pwd' : data['pwd'],
    }
    
    result = connect(data_list)
    
    returnData = result
    return JsonResponse(returnData)


@csrf_exempt
def navigator_api(request) :
    data = request.POST['name']
    qry = """
        select * from dbc.tables where databasename = '""" + data + """';
    """
    
    result = db_select(qry)
    returnData = {
                'status' : result['status'],
                'data' : result['data']['TableName'].values.tolist(),
                'ddl' : result['data']['RequestText'].values.tolist()
            }
    return JsonResponse(returnData)

@csrf_exempt
def property_api(request) :
    database = request.POST['database']
    table = request.POST['table']
    ddl = request.POST['ddl']
    
    data = str(database) +'.'+ str(table)
    print("=====================")
    print(data)
    print("=====================")
    
    qry = """
        select * from """ + data + """;
    """
    
    qry2= """
    SELECT 
        ColumnName, 
        Nullable,
        TRIM(CASE 
        WHEN COLUMNTYPE='CF' THEN 'CHAR'
        WHEN COLUMNTYPE='CV' THEN 'VARCHAR'
        WHEN COLUMNTYPE='D'  THEN 'DECIMAL' 
        WHEN COLUMNTYPE='TS' THEN 'TIMESTAMP'      
        WHEN COLUMNTYPE='I'  THEN 'INTEGER'
        WHEN COLUMNTYPE='I2' THEN 'SMALLINT'
        WHEN COLUMNTYPE='DA' THEN 'DATE'  
        END)||'('||TRIM(ColumnLength)||')' as ColumnType
    FROM 
        dbc."Columns" c 
    WHERE 
        DatabaseName ='"""+ database +"""' 
        and 
        TableName = '"""+ table +"""';
    """
    
    data = db_select(qry)
    columns = db_select(qry2)
    ddl = ddl.replace('<hr>', "'")
    
    returnData = {
                'status' : data['status'],
                'data' : data['data'].values.tolist(),
                'data_column' : data['data'].columns.values.tolist(),
                'columns' : columns['data'].values.tolist(),
                'columns_column' : columns['data'].columns.values.tolist(),
                'ddl' : ddl
            }
    return JsonResponse(returnData)

@csrf_exempt
def postgres_navigator_api(request) :
    data = request.POST['name']
    qry = """
        select * from dbc.tables where databasename = '""" + data + """';
    """
    
    result = db_select(qry)
    returnData = {
                'status' : result['status'],
                'data' : result['data']['TableName'].values.tolist(),
                'ddl' : result['data']['RequestText'].values.tolist()
            }
    return JsonResponse(returnData)
    

def connect_DBList():
    td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
    qry = """
        select 
            *
        from
            xfactor.connect_tera2
        """
    result = td_context.execute(qry)
    a = result.fetchall()

    a = pd.DataFrame(a).reset_index()
    a['index'] = a['index'].add(1)
    # print(a)
    dict = a.to_dict('records')

    return dict

