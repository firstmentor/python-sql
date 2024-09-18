import mysql.connector as Myconn

mydb =Myconn.connect(host="localhost",user="root",password="",database="pn123")
db_cursor = mydb.cursor() #cursor methord se hi sql queary chal payege


# db_cursor.execute('SELECT * FROM emp')

db_cursor.execute("SELECT * FROM emp WHERE roll =123")

myresult = db_cursor.fetchall()
print(myresult)

for x in myresult:
  print(x)


