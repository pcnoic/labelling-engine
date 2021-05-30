from posixpath import dirname
import sqlite3
from sqlite3 import Error
import os
from constants import DATABASES_PATH


class SQLiteWrapper:
    
    def new_working_dir():
        try:
            os.mkdir(DATABASES_PATH)
        except OSError:
            print("Creation of the directory %s failed" % DATABASES_PATH)
        else:
            print("Successfully created the directory %s " % DATABASES_PATH)    


    def get_db_path(db_name):
        dirname = os.path.dirname(__file__)
        db_path = os.path.join(dirname, DATABASES_PATH + "/" + db_name)

        return db_path


    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

        return conn

    
    def run_query(connection, query):
        try:
            c  = connection.cursor()
            c.execute(query)
        except Error as e:
            print(e)
            
    
    def close_connection(connection):
        connection.close()


class SQLiteCommonQueries:
    
    def new_create_query(table_name):
        sql_create_table = "CREATE TABLE IF NOT EXISTS " + table_name + """ (
                                        id text PRIMARY KEY,
                                        location text NOT NULL,
                                        integer text
                                    ); """
                                    
        return sql_create_table

    
    def new_drop_query(table_name):
        sql_drop_table = "DROP TABLE " + table_name
        
        return sql_drop_table
    
    
    def new_insert_query(table_name, columns, data):
        column_names = []
        datums = []
        for column in columns:
            column_names.append(column)
            column_names.append(",")
        
        for datum in data:
            datums.append(datum)
            datums.append(",")
            
        
        sql_insert_query = "INSERT INTO " + table_name + "("
        sql_insert_query.join(column_names)
        sql_insert_query = sql_insert_query + ")" + " VALUES("
        sql_insert_query.join(datums) + ")"
        
        return sql_insert_query
    