import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

with open('database.sql', 'r', encoding='utf-8') as file:
    cursor.executescript(file.read())

connection.commit()
connection.close()

print('Banco de dados criado com sucesso!')