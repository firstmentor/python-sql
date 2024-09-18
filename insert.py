import mysql.connector as Myconn

mydb =Myconn.connect(host="localhost",user="root",password="",database="pn123")
db_cursor = mydb.cursor() #cursor methord se hi sql queary chal payege

sql = "INSERT INTO emp (roll, ename) VALUES (%s, %s)"
val = (1234, "Highway 21")
dblist =[(12,"ram"),(123,"ram"),(1234,"ram"),(12233,"ram")]
#db_cursor.execute(sql, val)
db_cursor.executemany(sql, dblist)

mydb.commit()

print(db_cursor.rowcount, "record inserted.")


