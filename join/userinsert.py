import mysql.connector as Myconn

mydb =Myconn.connect(host="localhost",user="root",password="",database="pn123")
db_cursor = mydb.cursor() #cursor methord se hi sql queary chal payege

sql = "INSERT INTO users (id, name,fav) VALUES (%s, %s,%s)"
# val = (1, "name")
dblist =[(1,"ram",123),(2,"raj",56),(3,"rohit",34),(4,"av",45)]
#db_cursor.execute(sql, val)
db_cursor.executemany(sql, dblist)

mydb.commit()

print(db_cursor.rowcount, "record inserted.")


