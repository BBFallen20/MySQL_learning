from connection import database


cursor = database.cursor()

cursor.execute("CREATE DATABASE test_db")

print("Database created successfully.")
