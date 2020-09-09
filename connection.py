import mysql.connector

database = input("DB NAME:\n")

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='756756',
    database=database if database else None
)

