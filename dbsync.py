import mysql.connector

dbconfig = { 'host': 'notebook.cjwbzocqulu8.us-east-1.rds.amazonaws.com',
                'user': 'script',
                'password': 'script@123',
                'database': 'warehouse', }

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

_SQL = """insert into bitcoin(currency, price, date, time) values (%s, %s, %s, %s)"""
cursor.execute(_SQL, ('INR', '2345', '22-2-1988', '11:12:00'))
