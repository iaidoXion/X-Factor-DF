import teradataml
from sqlalchemy import *
from teradataml import *
from pprint import pprint
import pandas as pd
import psycopg2
def db_select(qry):    
    try :
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")   
        result = td_context.execute(qry)   
        data = result.fetchall()    
        data = pd.DataFrame(data)    
        data = data.fillna('NULL')
        print("===============================")
        print("Success")
        print("===============================")
        data = {'status' : 200, 'data' : data, 'type' : 'select'}
    except Exception as e :
        if 'Failed to connect to Teradata Vantage' in str(e) :
            data = {'status' : 404, 'data' : 'Failed to connect to Teradata Vantage', 'type' : 'select'}
        
        else :
            if '[Error' in str(e) :
                err_index = str(e).find('[Error')
                err_index = str(e).index(']', err_index)
                error = str(e)[0 : err_index]
                error_list = str(e).strip(error).split('at ')
                for i in range(len(error_list)) :
                    if i == 0 :
                        error_list[i] = 'S' + error_list[i]
                        continue
                    error_list[i] = 'at ' + error_list[i]
                error_list.insert(0, error + ']')
            data = {'status' : 400, 'data' : error_list, 'type' : 'select'}
        
    return  data

def db_create(qry):  
    try :
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")    

        result = td_context.execute(qry)    
        data = result.fetchall()
        
        print("===============================")
        print("Success")
        print("===============================")
        data = {'status' : 200, 'data' : qry.splitlines(), 'type' : 'create'}
    except Exception as e :
        if 'Failed to connect to Teradata Vantage' in str(e) :
            data = {'status' : 404, 'data' : 'Failed to connect to Teradata Vantage'}
        else :
            if '[Error' in str(e) :
                err_index = str(e).find('[Error')
                err_index = str(e).index(']', err_index)
                error = str(e)[0 : err_index]
                error_list = str(e).strip(error).split('at ')
                for i in range(len(error_list)) :
                    if i == 0 :
                        error_list[i] = 'S' + error_list[i]
                        continue
                    error_list[i] = 'at ' + error_list[i]
                error_list.insert(0, error + ']')
            data = {'status' : 400, 'data' : error_list, 'type' : 'create'}
    return data

def connect(data):
    if data['db'] == 'Teradata' :
        try :
            db = create_context(host="{}:{}".format(data['db_host'], data['db_port']),
                                        username = data['user_id'], 
                                        password = data['user_pwd'], 
                                        logmech="TD2")
            status = 200
            setting_insert(data)
            useraddress = str(db)
        except Exception as e :
            print("==================")
            print('연결실패')
            print("==================")
            status = 400
            useraddress = str(db)
    elif data['db'] == 'Postgres' :
        try :
            db = psycopg2.connect(host=data['db_host'], 
                                dbname = data['user_id'],
                                user = data['user_id'],
                                password = data['user_id'],
                                port = data['db_port'])
            status = 200
            setting_insert(data)
            useraddress = str(db)
        except Exception as e :
            print("==================")
            print('연결실패')
            print("==================")
            status = 400
            useraddress = str(e)
            
    result = {
        'status': status,
        'data': useraddress,
        'host': data['db_host'],
        'dbname': data['user_id'],
        'user': data['user_id'],
        'password': data['user_id'],
        'port': data['db_port']
    }
    print(result)
    return result

def setting_insert(data): #파라미터값 web_user 추가
    web_user = 'admin'
    td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
    # td_context = create_context(host="{}:{}".format(data['db_host'], data['db_port']),
    #                database=data['db_name'],
    #                username=data['user_id'],
    #                password=data['user_pwd'],
    #                logmech="TD2")
    qry = """
        INSERT INTO xfactor.connect_tera2
            (database_name, database_type, "host", port, web_user, db_user, db_pw)
        values
        ('"""+data['db_name']+"""','"""+data['db']+"""','"""+data['db_host']+"""','"""+data['db_port']+"""','"""+web_user+"""','"""+data['user_id']+"""','"""+data['user_pwd']+"""')
        """
    print(qry)
    result = td_context.execute(qry)
    print(result)

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
    #print(a)
    dict = a.to_dict('records')

    return dict