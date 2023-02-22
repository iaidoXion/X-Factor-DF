import teradataml
from sqlalchemy import *
from teradataml import *
from pprint import pprint
import pandas as pd
import psycopg2
import json
import unicodedata

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
DataLoadingType = SETTING['MODULE']['DataLoadingType']
DBType = SETTING['DB']['DBType']
DBHost = SETTING['DB']['DBHost']
DBPort = SETTING['DB']['DBPort']
DBName = SETTING['DB']['DBName']
DBUser = SETTING['DB']['DBUser']
DBPwd = SETTING['DB']['DBPwd']
HistoryTNM = SETTING['DB']['HistoryTNM']
UserTNM = SETTING['DB']['UserTNM']
Login_Method = SETTING['PROJECT']['LOGIN']

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
    qry = qry.lower()
    dbname = DBName
    dbtype = DBType
    table = ''
    web_user = 'admin' #나중에 세션값
    db_user = DBUser
    db_query = qry
    db_result = ''

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
def db_insert(qry):
    try:
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")

        result = td_context.execute(qry)
        data = result.fetchall()

        print("===============================")
        print("Success")
        print("===============================")
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create'}
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
            data = {'status': 400, 'data': error_list, 'type': 'create'}
    return data

def db_update(qry):
    try:
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")

        result = td_context.execute(qry)
        data = result.fetchall()

        print("===============================")
        print("Success")
        print("===============================")
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create'}
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
            data = {'status': 400, 'data': error_list, 'type': 'create'}
    return data

def db_delete(qry):
    try:
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")

        result = td_context.execute(qry)
        data = result.fetchall()

        print("===============================")
        print("Success")
        print("===============================")
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create'}
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
            data = {'status': 400, 'data': error_list, 'type': 'create'}
    return data

def db_drop(qry):
    try:
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")

        result = td_context.execute(qry)
        data = result.fetchall()

        print("===============================")
        print("Success")
        print("===============================")
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create'}
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
            data = {'status': 400, 'data': error_list, 'type': 'create'}
    return data

def db_rename(qry):
    try:
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")

        result = td_context.execute(qry)
        data = result.fetchall()

        print("===============================")
        print("Success")
        print("===============================")
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create'}
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
            data = {'status': 400, 'data': error_list, 'type': 'create'}
    return data

def db_alter(qry):
    try:
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")

        result = td_context.execute(qry)
        data = result.fetchall()

        print("===============================")
        print("Success")
        print("===============================")
        data = {'status': 200, 'data': qry.splitlines(), 'type': 'create'}
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
            data = {'status': 400, 'data': error_list, 'type': 'create'}
    return data
def db_show(qry):
    qry=qry.lower()
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
    result = td_context.execute(qry)

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


def history_insert(data):
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

        return DC
    except:
        print(HistoryTNM + ' History Table connection(Select) Failure')


def database_traffic():
    try:
        td_context = create_context(host=DBHost + ":" + DBPort, username=DBUser, password=DBPwd)
        query = """
               select 
                   database_name, count(*)
               from
                   """ + DBName + """.""" + HistoryTNM + """
                group by database_name;

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
        #print(DC)
        return DC
    except:
        print(HistoryTNM + ' History Table connection(Select) Failure')

def user_traffic ():
    try:
        td_context = create_context(host=DBHost + ":" + DBPort, username=DBUser, password=DBPwd)
        query = """
               select 
                   db_user, count(*)
               from
                   """ + DBName + """.""" + HistoryTNM + """
                group by db_user;

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
        #print(DC)
        return DC
    except:
        print(HistoryTNM + ' History Table connection(Select) Failure')

