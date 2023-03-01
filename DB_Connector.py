import mysql.connector

class DB_Connector():
    def __init__(self):
        self.db = mysql.connector.connect(
                user='root',
                password='LDLink16',
                host='127.0.0.1',
                port='3306'
        )

        self.cursor = self.db.cursor()
        
        self.cursor.exectute('CREATE DATABASE foo')
        self.cursor.exectute('CREATE DATABASE bar')
        self.cursor.exectute('SHOW DATABASES')

        for db in self.cursor:
            print(db)
