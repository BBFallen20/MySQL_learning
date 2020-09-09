from connection import database


cursor = database.cursor()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute("SELECT name FROM users")

rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute("SELECT age FROM users")

rows = cursor.fetchall()

for row in rows:
    print(row)
