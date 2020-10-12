
# All CRUD DB routines are stored here

import sqlite3
from sqlite3 import Error
pwd_dbname = "ArunsPasswordDB"
pwd_table = 'PWD_TABLE'

#def open_connection(pwd_dbname):
# return(cursor)

def Update_DB(*dbparams):
    DB_option_dict = {
        "c": [], "s":  [], "u":[], "d":[], "q":[] }
    try:
       sqliteConnection = sqlite3.connect(pwd_dbname)
       cursor = sqliteConnection.cursor()
       print("Connected to SQLite")
       insertVariableIntoTable(create_list[0], create_list[1], create_list[2], create_list[3], create_list[4])
       sqliteConnection.commit()
       cursor.close()
       return
    except sqlite3.Error as error:
        print("DB Operation into PWD_TABLE with Python variable failed", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
    

#***************************************************************************************
def insertVariableIntoTable(svc_name, user_id, password, stype, comments):
    
        sqlite_insert_with_param = """INSERT INTO PWD_TABLE
                          (svc_name, user_id, password, stype, comments) 
                          VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (svc_name, user_id, password, stype, comments)
        cursor.execute(sqlite_insert_with_param, data_tuple)
       
  #**********************************************************************************************
def readSingleRow(developerId):
   
        sqlite_select_query = """SELECT * from PWD_TABLE where id = ?"""
        cursor.execute(sqlite_select_query, developerId)
        print("Reading single row \n")

#*********************************************************************************************
def updateSingleRow(svc_name, user_id, password, stype, comments)    
 sql_update_query = """Update SqliteDb_developers set salary = ? where id = ?"""
        data = (salary, id)
        cursor.execute(sql_update_query, data)
         
#********************************************************************************************************

def create_pwd(option):
    msg_list = ["Enter service name","Enter user id", "Enter password", "Enter type", "Enter comments if any"]
    create_list = [].append(option)
    i=0
    while i < len(msg_list):
        print(msg_list[i])
        create_list.append(input().strip())
        i+=1
#print(create_list)
        Update_DB(create_list)
        return

def  show_pwd():
    print("Enter Service name")
    sname = input().strip()
    lookupVariableInTable(sname)
if __name__ == '__main__':
     create_pwd('c')

