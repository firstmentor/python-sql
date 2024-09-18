import mysql.connector as Myconn

mydb =Myconn.connect(host="localhost",user="root",password="",database="pn123")
db_cursor = mydb.cursor() #cursor methord se hi sql queary chal payege




#sql = "DROP TABLE emp"
sql ="truncate table emp"

db_cursor.execute(sql)


print(db_cursor.rowcount,"All Record deleted")