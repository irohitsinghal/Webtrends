import mysql.connector

dbconfig = { 'host': 'notebook.cjwbzocqulu8.us-east-1.rds.amazonaws.com',
                'user': 'script',
                'password': 'script@123',
                'database': 'warehouse', }

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

#_SQL = """insert into bitcoin(currency, price, date, time) values (%s, %s, %s, %s)"""
#cursor.execute(_SQL, ('INR', '2345', '1988-02-22', '11:12:00'))
_SQL = """select * from  bitcoin"""
cursor.execute(_SQL)
print(cursor.fetchall())
