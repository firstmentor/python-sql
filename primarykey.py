import mysql.connector as Myconn

mydb =Myconn.connect(host="localhost",user="root",password="",database="pn123")
db_cursor = mydb.cursor() #cursor methord se hi sql queary chal payege
# Create a cursor object


# db_cursor.execute('create table users(id int,name varchar(20),fav varchar(50))')
# db_cursor.execute('CREATE TABLE pn1(Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(50))')
# print("table created")


sql = "INSERT INTO pn1 (name) VALUES (%s)"
# val = ("raj",)
dblist =[("ram")]
# db_cursor.execute(sql, val)
db_cursor.executemany(sql, dblist)

mydb.commit()

print(db_cursor.rowcount, "record inserted.")




# db_cursor.execute('show tables')
# for i in db_cursor:
#     print(i)
