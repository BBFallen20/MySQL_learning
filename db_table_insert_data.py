from connection import database


cursor = database.cursor()

sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
val = [
    ('Paul', 22),
    ('John', 41),
    ('Ben', 29)
]

cursor.executemany(sql, val)

database.commit()

print(f"{cursor.rowcount} rows was successfully inserted.")
