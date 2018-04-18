import sqlite3
import mysql.connector
from mysql.connector import MySqlConnection, Error

class MySQLiteConnection:
    def __init__(self, db = sqlite3.connect('test.db')):
        self.db = db
        db.row_factory = sqlite3.Row
        print("connected to SQLite3")
    def Retrieve(self):
        print("retrieving values form table test1 of Sqlite database", db)
        read = self.db.execute('select * from test1 order by i1')
        for row in read:
            print(row['t1'])

class MyMySQLConnection:
    def __init__(self, kwargs = dict(
        host = 'localhost',
        database = 'testdb',
        user = 'root',
        password = 'pass'
        )):
            try:
                #using dictionary object
                self.kwargs = kwargs
                conn = mysql.connector.connect(**kwargs)
                if conn.is_connected():
                    print("connected to MySQL database", database, "from 'conn' object")
            except Error as e:
                print(e)
            finally:
                conn.close()
    def Retrieve(self):
            print("retrieving records from MySQL database", database)
            try:
                conn = MyMySQLConnection(**self.kwargs)
                cursor = conn.cursos()
                cursor.execute("SELECT * FROM EMPLOYEE")
                rows = cursor.fetchall()
                print("total row(s): ", cursor.rowcount)
                for row in rows:
                    print("first name: ", row[0])
                    print("second name: ", row[1])
                    print("age: ", row[2])
                    print("sex: ", row[3])
                    print("salary: ", row[4])
            except Error as e:
                print(e)
            finally:
                cursor.close()
                conn.close()
            def main():
                ConnectToMySQL = MyMySQLConnection()
                ConnectToMySQL.Retrieve()
                ConnectToMySQLite = MySQLiteConnection()
                ConnectToMySQLite.Retrieve()
                    