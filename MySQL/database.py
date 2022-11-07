import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='elena',
    password='elena',
    database='testdb',
    )

#print(mydb)

my_cursor=mydb.cursor() #Initializing the cursor

#Creating a database

#my_cursor.execute('CREATE DATABASE testdb')

#my_cursor.execute('SHOW DATABASES')

#print(my_cursor) #it shows only the command SHOW DATABASE

#for db in my_cursor:
#    print(db[0])

#Creating a table in a database

#my_cursor.execute('CREATE TABLE users (name VARCHAR(255),email VARCHAR(255),age INTEGER(10),user_id INTEGER AUTO_INCREMENT PRIMARY KEY)')
#my_cursor.execute('SHOW TABLES')
#for table in my_cursor:
#    print(table[0])

#Inserting data into the table

sqlStuff='INSERT INTO users (name,email,age) VALUES (%s,%s,%s)'
record1=('John','john@codemy.com',40)

my_cursor.execute(sqlStuff,record1)
mydb.commit()









