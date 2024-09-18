import mysql.connector as Myconn

mydb =Myconn.connect(host="localhost",user="root",password="",database="pn123")
db_cursor = mydb.cursor() #cursor methord se hi sql queary chal payege
db_cursor.execute('create table emp(roll int,ename varchar(20))')
print("table created")

# db_cursor.execute('show tables')
# for i in db_cursor:
#     print(i)
