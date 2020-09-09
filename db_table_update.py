from connection import database


cursor = database.cursor()


cursor.execute("UPDATE users SET age = '20' WHERE name = 'Paul'")


database.commit()

