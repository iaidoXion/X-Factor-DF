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
        print(data.columns)
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
            td_context = create_context(host="{}:{}".format(data['db_host'], data['db_port']), 
                                        username = data['user_id'], 
                                        password = data['user_pwd'], 
                                        logmech="TD2")
        except Exception as e :
            print("==================")
            print('연결실패')
            print("==================")
            status = 400
            data = str(db)
    elif data['db'] == 'Postgres' :
        try :
            db = psycopg2.connect(host=data['db_host'], 
                                dbname = data['user_id'],
                                user = data['user_id'],
                                password = data['user_id'],
                                port = data['db_port'])
            status = 200
            data = str(db)
        except Exception as e :
            print("==================")
            print('연결실패')
            print("==================")
            status = 400
            data = str(e)
            
    result = {
        'status' : status,
        'data' : data
    }
    return result