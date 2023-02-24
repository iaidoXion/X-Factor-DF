import teradataml
from sqlalchemy import *
from teradataml import *
from pprint import pprint
import pandas as pd
import psycopg2
import json
import unicodedata
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import binascii

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
DataLoadingType = SETTING['MODULE']['DataLoadingType']
DBType = SETTING['DB']['DBType']
DBHost = SETTING['DB']['DBHost']
DBPort = SETTING['DB']['DBPort']
DBName = SETTING['DB']['DBName']
DBUser = SETTING['DB']['DBUser']
DBPwd = SETTING['DB']['DBPwd']
StatisticsTNM = SETTING['DB']['StatisticsTNM']
HistoryTNM = SETTING['DB']['HistoryTNM']
UserTNM = SETTING['DB']['UserTNM']
Login_Method = SETTING['PROJECT']['LOGIN']
monthDay = (datetime.today() - relativedelta(days=31)).strftime("%Y-%m-%d")

def db_select(qry):
    qry=qry.lower()
    dbname = DBName
    dbtype = DBType
    table = ' '
    web_user = 'admin'#나중에 세션값
    db_user = DBUser
    db_query = qry
    db_result = ''
    try :
        history = []
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
        result = td_context.execute(qry)
        data = result.fetchall()
        data = pd.DataFrame(data)
        data = data.fillna('NULL')
        #print(data)
        #print(data['UserId'])
        #valid_png_header = data['UserId'][2]
        #print(valid_png_header)
        #print(type(valid_png_header))
        #encoding = sys.getdefaultencoding()
        #s = valid_png_header.decode(encoding)
        #print(s)
        #print(valid_png_header.decode('utf-16'))
        #print(binascii.hexlify(valid_png_header))
        #valid_png_header2 = binascii.hexlify(valid_png_header)
        #valid_png_header3 = str(valid_png_header2, 'cp949')
        #print(str(valid_png_header2, 'cp949'))
        #code = (valid_png_header2, 'cp949')
        #print(code)
        #code.decode("hex")
        #print(binascii.unhexlify(valid_png_header3))
        #print(valid_png_header.decode('hex'))
        #print(binascii.a2b_base64(valid_png_header))
        for key, value in data.iteritems():
            print(key)
            print(type(data[key][0]))
            if type(data[key][0]) == type(bytes(1)):
                for key2, value2 in data[key].iteritems():
                    print(data[key][key2])
                    valid_png_header = data[key][key2]
                    #valid_png_header2 = str(data['UserId'][key], 'utf-8')
                    #print(valid_png_header)
                    try:
                        data[key][key2] = valid_png_header.decode('utf-16')
                    except:
                        pass
            else:
                 continue
                # data['UserId'][key] = binascii.a2b_base64(valid_png_header)
                # print(data['UserId'][key])
        #print(data['UserId'])
        print("===============================")
        print("Success")
        print("===============================")
        table = qry.split('from ')[1].split(' ')[0]
        db_result = "Success SELECT Table Rows "+table
        history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
        data = {'status' : 200, 'data' : data, 'type' : 'select', 'history': history}
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
            db_result = "Fail SELECT Table "
            history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
            data = {'status': 400, 'data': error_list, 'type': 'select', 'history': history}
    remove_context()
    history_insert(data)
    return  data

def db_create(qry):
    qry = qry.lower()
    dbname = DBName
    dbtype = DBType
    table = ''
    web_user = 'admin' #나중에 세션값
    db_user = DBUser
    db_query = qry
    db_result = ''
    try :
        history = []
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
        result = td_context.execute(qry)
        data = result.fetchall()
        table = qry.split('table ')[1].split(' ')[0]
        db_result = "Success CREATE Table Rows " + table
        print("===============================")
        print("Success")
        print("===============================")
        history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create', 'history': history}
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
            db_result = "Fail CREATE Table "
            history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
            data = {'status': 400, 'data': error_list, 'type': 'create', 'history': history}
    remove_context()
    history_insert(data)
    return data
def db_insert(qry):
    qry = qry.lower()
    dbname = DBName
    dbtype = DBType
    table = ''
    web_user = 'admin' #나중에 세션값
    db_user = DBUser
    db_query = qry
    db_result = ''
    try:
        history = []
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
        result = td_context.execute(qry)
        data = result.fetchall()
        table = qry.split('into ')[1].split(' ')[0]
        db_result = "Success INSERT Table Rows " + table
        print("===============================")
        print("Success")
        print("===============================")
        history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create', 'history': history}
    except Exception as e:
        if 'Failed to connect to Teradata Vantage' in str(e):
            data = {'status': 404, 'data': 'Failed to connect to Teradata Vantage'}
        else:
            if '[Error' in str(e):
                err_index = str(e).find('[Error')
                err_index = str(e).index(']', err_index)
                error = str(e)[0: err_index]
                error_list = str(e).strip(error).split('at ')
                for i in range(len(error_list)):
                    if i == 0:
                        error_list[i] = 'S' + error_list[i]
                        continue
                    error_list[i] = 'at ' + error_list[i]
                error_list.insert(0, error + ']')
            db_result = "Fail INSERT Table "
            history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
            data = {'status': 400, 'data': error_list, 'type': 'create', 'history': history}
    remove_context()
    history_insert(data)
    return data

def db_update(qry):
    qry=qry.lower()
    dbname = DBName
    dbtype = DBType
    table = ''
    web_user = 'admin' #나중에 세션값
    db_user = DBUser
    db_query = qry
    db_result = ''
    try:
        history = []
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
        result = td_context.execute(qry)
        data = result.fetchall()
        table = qry.split('update ')[1].split(' ')[0]
        db_result = "Success UPDATE Table Rows " + table
        print("===============================")
        print("Success")
        print("===============================")
        history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create', 'history': history}
    except Exception as e:
        if 'Failed to connect to Teradata Vantage' in str(e):
            data = {'status': 404, 'data': 'Failed to connect to Teradata Vantage'}
        else:
            if '[Error' in str(e):
                err_index = str(e).find('[Error')
                err_index = str(e).index(']', err_index)
                error = str(e)[0: err_index]
                error_list = str(e).strip(error).split('at ')
                for i in range(len(error_list)):
                    if i == 0:
                        error_list[i] = 'S' + error_list[i]
                        continue
                    error_list[i] = 'at ' + error_list[i]
                error_list.insert(0, error + ']')
            db_result = "Fail UPDATE Table "
            history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
            data = {'status': 400, 'data': error_list, 'type': 'create', 'history': history}
    remove_context()
    history_insert(data)
    return data

def db_delete(qry):
    qry=qry.lower()
    dbname = DBName
    dbtype = DBType
    table = ''
    web_user = 'admin'#나중에 세션값
    db_user = DBUser
    db_query = qry
    db_result = ''
    try:
        history = []
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
        result = td_context.execute(qry)
        data = result.fetchall()
        table = qry.split('from ')[1].split(' ')[0]
        db_result = "Success DELETE Table Rows " + table
        print("===============================")
        print("Success")
        print("===============================")
        history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create', 'history': history}
    except Exception as e:
        if 'Failed to connect to Teradata Vantage' in str(e):
            data = {'status': 404, 'data': 'Failed to connect to Teradata Vantage'}
        else:
            if '[Error' in str(e):
                err_index = str(e).find('[Error')
                err_index = str(e).index(']', err_index)
                error = str(e)[0: err_index]
                error_list = str(e).strip(error).split('at ')
                for i in range(len(error_list)):
                    if i == 0:
                        error_list[i] = 'S' + error_list[i]
                        continue
                    error_list[i] = 'at ' + error_list[i]
                error_list.insert(0, error + ']')
            db_result = "Fail DELETE "
            history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
            data = {'status' : 400, 'data' : error_list, 'type' : 'create','history': history}
    remove_context()
    history_insert(data)
    return data

def db_drop(qry):
    qry=qry.lower()
    dbname = DBName
    dbtype = DBType
    table = ''
    web_user = 'admin'  # 나중에 세션값
    db_user = DBUser
    db_query = qry
    db_result = ''
    try:
        history = []
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
        result = td_context.execute(qry)
        data = result.fetchall()
        table = qry.split('table ')[1].split(' ')[0]
        db_result = "Success DROP Table Rows " + table
        print("===============================")
        print("Success")
        print("===============================")
        history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
        data = {'status' : 200, 'data' : qry.splitlines(), 'type' : 'create','history': history}
    except Exception as e:
        if 'Failed to connect to Teradata Vantage' in str(e):
            data = {'status': 404, 'data': 'Failed to connect to Teradata Vantage'}
        else:
            if '[Error' in str(e):
                err_index = str(e).find('[Error')
                err_index = str(e).index(']', err_index)
                error = str(e)[0: err_index]
                error_list = str(e).strip(error).split('at ')
                for i in range(len(error_list)):
                    if i == 0:
                        error_list[i] = 'S' + error_list[i]
                        continue
                    error_list[i] = 'at ' + error_list[i]
                error_list.insert(0, error + ']')
            db_result = "Fail DROP Table "
            history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
            data = {'status' : 400, 'data' : error_list, 'type' : 'create' ,'history': history}
    remove_context()
    history_insert(data)
    return data

def db_rename(qry):
    qry=qry.lower()
    dbname = DBName
    dbtype = DBType
    table = ''
    web_user = 'admin'  # 나중에 세션값
    db_user = DBUser
    db_query = qry
    db_result = ''
    try:
        history = []
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
        result = td_context.execute(qry)
        data = result.fetchall()
        table = qry.split('table ')[1].split(' ')[0]
        db_result = "Success RENAME Table Rows " + table
        print("===============================")
        print("Success")
        print("===============================")
        history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
        data = {'status' : 200, 'data' : qry.splitlines(), 'type' : 'create','history': history}
    except Exception as e:
        if 'Failed to connect to Teradata Vantage' in str(e):
            data = {'status': 404, 'data': 'Failed to connect to Teradata Vantage'}
        else:
            if '[Error' in str(e):
                err_index = str(e).find('[Error')
                err_index = str(e).index(']', err_index)
                error = str(e)[0: err_index]
                error_list = str(e).strip(error).split('at ')
                for i in range(len(error_list)):
                    if i == 0:
                        error_list[i] = 'S' + error_list[i]
                        continue
                    error_list[i] = 'at ' + error_list[i]
                error_list.insert(0, error + ']')
            db_result = "Fail RENAME Table "
            history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
            data = {'status' : 400, 'data' : error_list, 'type' : 'create' ,'history': history}
    remove_context()
    history_insert(data)
    return data

def db_alter(qry):
    qry=qry.lower()
    dbname = DBName
    dbtype = DBType
    table = ''
    web_user = 'admin' #나중에 세션값
    db_user = DBUser
    db_query = qry
    db_result = ''
    try:
        history = []
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
        result = td_context.execute(qry)
        data = result.fetchall()
        table = qry.split('table ')[1].split(' ')[0]
        db_result = "Success ALTER Table Rows " + table
        print("===============================")
        print("Success")
        print("===============================")
        history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create', 'history': history}
    except Exception as e:
        if 'Failed to connect to Teradata Vantage' in str(e):
            data = {'status': 404, 'data': 'Failed to connect to Teradata Vantage'}
        else:
            if '[Error' in str(e):
                err_index = str(e).find('[Error')
                err_index = str(e).index(']', err_index)
                error = str(e)[0: err_index]
                error_list = str(e).strip(error).split('at ')
                for i in range(len(error_list)):
                    if i == 0:
                        error_list[i] = 'S' + error_list[i]
                        continue
                    error_list[i] = 'at ' + error_list[i]
                error_list.insert(0, error + ']')
            db_result = "Fail ALTER Table "
            history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
            data = {'status': 400, 'data': error_list, 'type': 'create', 'history': history}
    remove_context()
    history_insert(data)
    return data
def db_show(qry):
    qry=qry.lower()
    dbname = DBName
    dbtype = DBType
    table = ''
    web_user = 'admin' #나중에 세션값
    db_user = DBUser
    db_query = qry
    db_result = ''
    try :
        history = []
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
        result = td_context.execute(qry)
        data = result.fetchall()
        data = pd.DataFrame(data)
        data = data.fillna('NULL')
        table = qry.split('table ')[1].split(' ')[0]
        db_result = "Success SHOW Table Rows " + table
        print("===============================")
        print("Success")
        print("===============================")
        history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
        data = {'status': 200, 'data': data, 'type': 'show', 'history': history}
    except Exception as e :
        if 'Failed to connect to Teradata Vantage' in str(e) :
            data = {'status' : 404, 'data' : 'Failed to connect to Teradata Vantage', 'type' : 'show'}
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
            db_result = "Fail SHOW Table "
            history = [dbname, dbtype, table, web_user, db_user, db_query, db_result]
            data = {'status' : 400, 'data' : error_list, 'type' : 'select' ,'history': history}
    remove_context()
    history_insert(data)
    return  data
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

    remove_context()
    
    result = {
        'status': status,
        'data': useraddress,
        'host': data['db_host'],
        'dbname': data['user_id'],
        'user': data['user_id'],
        'password': data['user_id'],
        'port': data['db_port']
    }
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
        INSERT INTO xfactor.connect_tera
            (database_name, database_type, "host", port, web_user, db_user, db_pw)
        values
        ('"""+data['db_name']+"""','"""+data['db']+"""','"""+data['db_host']+"""','"""+data['db_port']+"""','"""+web_user+"""','"""+data['user_id']+"""','"""+data['user_pwd']+"""')
        """
    result = td_context.execute(qry)

def connect_DBList():
    td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
    qry = """
        select 
            *
        from
            xfactor.connect_tera
        """
    result = td_context.execute(qry)
    a = result.fetchall()
    a = pd.DataFrame(a).reset_index()
    a['index'] = a['index'].add(1)
    #print(a)
    dict = a.to_dict('records')
    return dict


def history_insert(data):
    try:
        dbname=data['history'][0]
        dbtype=data['history'][1]
        dbtable=data['history'][2]
        webuser=data['history'][3]
        dbuser=data['history'][4]
        dbquery=data['history'][5].replace('\'','"')
        dbresult=data['history'][6]
        qry="""
            insert into """+DBName+"""."""+HistoryTNM+"""("database_name", "database_type", "db_table", "web_user", "db_user", "db_query", "db_result", "commit_date")
            values('"""+dbname+"""','"""+dbtype+"""','"""+dbtable+"""','"""+webuser+"""','"""+dbuser+"""','"""+dbquery+"""','"""+dbresult+"""',now());
        """
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")
        result = td_context.execute(qry)
        remove_context()
    except:
        print(HistoryTNM + ' History Table connection(Select) Failure')

def history_select():
    try:
        td_context = create_context(host=DBHost + ":" + DBPort, username=DBUser, password=DBPwd)
        query = """
            select
                *
            from
                """ + DBName + """.""" + HistoryTNM + """

            """
        result = td_context.execute(query)
        RS = result.fetchall()
        DFL = []
        for d in RS:
            num = d[0]
            dbname = d[1]
            dbtype = d[2]
            dbtable = d[3]
            web_user = d[4]
            db_user = d[5]
            db_query = d[6]
            db_result = d[7]
            commit_time = d[8]
            DFL.append([num, dbname, dbtype, dbtable, web_user, db_user, db_query, db_result, commit_time])
            DFC = ['num', 'dbname', 'dbtype', 'dbtable', 'web_user', 'db_user', 'db_query', 'db_result', 'commit_time']
        DF = pd.DataFrame(DFL, columns=DFC).sort_values(by='commit_time', ascending=False).reset_index(drop=True)
        DC = DF.to_dict('records')
        remove_context()
        return DC
    except:
        print(HistoryTNM + ' History Table connection(Select) Failure')


def database_traffic():
    try:
        td_context = create_context(host=DBHost + ":" + DBPort, username=DBUser, password=DBPwd)
        query ="""
               select top 5
                    database_name, count(*)
               from
                    """ + DBName + """.""" + HistoryTNM + """
               group by 
                    database_name
               order by
                    count(*) desc;
               """
        result = td_context.execute(query)
        RS = result.fetchall()
        DFL = []
        for d in RS:
            dbname = d[0]
            count = d[1]
            DFL.append([dbname, count])
            DFC = ['dbname', 'count']
        DF = pd.DataFrame(DFL, columns=DFC).sort_values(by="count", ascending=False).reset_index(drop=True)
        DC = DF.to_dict('records')
        remove_context()
        return DC
    except:
        print(HistoryTNM + ' History Table connection(Select) Failure')

def user_traffic ():
    try:
        td_context = create_context(host=DBHost + ":" + DBPort, username=DBUser, password=DBPwd)
        query = """
               select top 5
                   db_user, count(*)
               from
                   """ + DBName + """.""" + HistoryTNM + """
                group by 
                    db_user
                order by
                    count(*) desc;
               """

        result = td_context.execute(query)
        RS = result.fetchall()
        DFL = []
        for d in RS:
            db_user = d[0]
            count = d[1]
            DFL.append([db_user, count])
            DFC = ['db_user', 'count']
        DF = pd.DataFrame(DFL, columns=DFC).sort_values(by="count", ascending=False).reset_index(drop=True)
        DC = DF.to_dict('records')
        remove_context()
        return DC
    except:
        print(HistoryTNM + ' History Table connection(Select) Failure')


def cpu_traffic():
    try:
        td_context = create_context(host=DBHost + ":" + DBPort, username=DBUser, password=DBPwd)
        query = """
               select 
                    item, 
                    item_count, 
                    statistics_collection_date
               from
                   """ + DBName + """.""" + StatisticsTNM + """
               where 
                    to_char(statistics_collection_date, 'YYYY-MM-DD') > '""" + monthDay + """' 
                and
                    classification = 'CPU_USAGE'
                 order by
                    statistics_collection_date ASC;
               """
        result = td_context.execute(query)
        RS = result.fetchall()
        DFL = []
        for d in RS:
            item = d[0]
            item_count = d[1]
            statistics_collection_data = d[2]
            DFL.append([item, item_count ,statistics_collection_data])
            DFC = ['item', 'item_count', 'statistics_collection_data']
        DF = pd.DataFrame(DFL, columns=DFC).sort_values(by="item", ascending=False).reset_index(drop=True)
        #print(DF)
        remove_context()
        #return DF
        T_count = []
        date_list = []
        P_count = []
        for i in range(len(DF)):
            if DF['item'][i] == 'teradata':
                T_count.append(DF['item_count'][i])
            else:
                P_count.append(DF['item_count'][i])
                date_list.append(str(DF['statistics_collection_data'][i]).split(' ')[0])
        ChartDataList = [{"data": [{"name": "TERADATA", "data": T_count}, {"name": "POSTGRES", "data": P_count}], "date": date_list}]
        #print(ChartDataList)
        return ChartDataList
    except:
        print(HistoryTNM + ' History Table connection(Select) Failure')