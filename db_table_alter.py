from connection import database


cursor = database.cursor()

cursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY ")

