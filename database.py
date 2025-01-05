import mysql.connector as Myconn

mydb =Myconn.connect(host="localhost",user="root",password="")  #mydb ek object hai

# print(mydb)
# print(mydb,"connect Establisted")

db_cursor = mydb.cursor() #cursor methord se hi sql queary chal payege function

db_cursor.execute('create database pn123')

print("Database Created")