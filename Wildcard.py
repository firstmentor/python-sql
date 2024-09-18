import mysql.connector as Myconn

mydb =Myconn.connect(host="localhost",user="root",password="",database="pn123")
db_cursor = mydb.cursor() #cursor methord se hi sql queary chal payege



sql = "SELECT * FROM emp WHERE ename LIKE '%ram%'"

db_cursor.execute(sql)

myresult = db_cursor.fetchall()

# for x in myresult:
#   print(x)
