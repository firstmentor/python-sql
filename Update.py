import mysql.connector as Myconn

mydb =Myconn.connect(host="localhost",user="root",password="",database="pn123")
db_cursor = mydb.cursor() #cursor methord se hi sql queary chal payege



sql = "UPDATE emp SET roll = '451   ' WHERE ename = 'ram'"

db_cursor.execute(sql)

mydb.commit()

print(db_cursor.rowcount, "record(s) affected")
