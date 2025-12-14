import mysql.connector



try:
    db = mysql.connector.connect(
        host = "localhost",
        user = "user",
        password = ""
    )
    print("Connection Successful")
except Exception as e:
    print(e)
    print("Connection failed")

try:
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE alx_book_store IF NOT EXISTS")
    print("Database 'alx_book_store' created successfully!")
except Exception as e:
    print("Database 'alx_book_store' failed ")