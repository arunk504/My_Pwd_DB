
# All CRUD DB routines are stored here

import sqlite3
from sqlite3 import Error
pwd_dbname = "ArunsPasswordDB"
pwd_table = 'PWD_TABLE'

#def open_connection(pwd_dbname):
# return(cursor)

#**********************************************************************************************
def readSingleRow(cursor, svc_name):
        print("Reading single row \n")
        sqlite_select_query = """SELECT * from PWD_TABLE where Account = ?"""
        cursor.execute(sqlite_select_query, (svc_name,))
        record = cursor.fetchone()
        if record:
            #print(record)
            return record
        else:
            return False
        
#*********************************************************************************************

def insertVariableIntoTable(cursor, svc_name, user_id, password, stype, comments):

    print(svc_name, " ", user_id, " ", password, " ", stype, " ", comments)
    sqlite_insert_with_param = """INSERT INTO PWD_TABLE
                          (Account, UserId, Password, PIN, Type) 
                          VALUES (?, ?, ?, ?, ?)"""

    data_tuple = (svc_name, user_id, password, stype, comments)
    if readSingleRow(cursor, svc_name):
        print("Account already exists, only updates allowed")
    else:
        cursor.execute(sqlite_insert_with_param, data_tuple)
#**************************************************************************************      
def updateSingleRow(cursor, svc_name, password):
    cursor.execute(sql_update_query, inputData)
    sql_update_query = """Update PWD_TABLE set Password = ? where Account = ?"""
    data = (svc_name, password)
    cursor.execute(sql_update_query, data)
    
#***************************************************************************************************
def deleteVariablefromTable(cursor, Account):
    print("Inside deleteVariable  ", Account)
    sql_Delete_query = """Delete from PWD_TABLE where Account = ?"""
    if readSingleRow(cursor, Account):
        print("Confirm delete (y/n):")
        option = input().strip().lower()
        if (option != 'y' ):
            cursor.close()
            return
        else:
            cursor.execute(sql_Delete_query, (Account,))
    else:
          return 0
#***************************************************************************************************            
def Update_DB(option,*dbparams):
    print("Inside update DB")
    print(option)
    
    try:
       sqliteConnection = sqlite3.connect(pwd_dbname)
       cursor = sqliteConnection.cursor()
       print("Connected to SQLite")
       if option == 'c':
            vals = dbparams[0][0:]
            insertVariableIntoTable(cursor, vals[0], vals[1], vals[2], vals[3], vals[4])
            print("Inserted row")
       elif option == 'd':
            deleteVariablefromTable(cursor, dbparams[0])
       elif option == 's':
            record= readSingleRow(cursor, dbparams[0])
            cursor.close()
            return record
       elif option == 'u':
            updateSingleRow(cursor,dbparams[0],dbparams[1])
       sqliteConnection.commit()
       cursor.close()
       return
    except sqlite3.Error as error:
        print("DB Operation into PWD_TABLE with Python variable failed", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
    
#******************************************************************************************************
def create_pwd(option):
    msg_list = ["Enter service name","Enter user id", "Enter password", "Enter type", "Enter comments if any"]
    create_list = []
    for x in msg_list:
        print(x)
        create_list.append(input().strip())
    #print(create_list)
    Update_DB(option, create_list)
    return

def  delete_pwd(option):
    print("Enter Service name")
    sname = input().strip()
    Update_DB(option, sname)
    
if __name__ == '__main__':
     delete_pwd('d')

