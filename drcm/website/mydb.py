import mysql.connector

database =mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd= 'Sedmeshach@747',
)


#prepare a cursor object
cursorObject =database.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE CodeCraft")

print("all Done!")