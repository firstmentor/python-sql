import mysql.connector as Myconn

mydb =Myconn.connect(host="localhost",user="root",password="",database="pn123")
db_cursor = mydb.cursor() #cursor methord se hi sql queary chal payege

sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
# val = (1, "name")
dblist =[(123,"ram"),(56,"raj"),(57,"rohit")]
#db_cursor.execute(sql, val)
db_cursor.executemany(sql, dblist)

mydb.commit()

print(db_cursor.rowcount, "record inserted.")


