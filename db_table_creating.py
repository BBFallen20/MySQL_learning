from connection import database


cursor = database.cursor()

cursor.execute("CREATE TABLE users (name VARCHAR(255), age INT(255))")


