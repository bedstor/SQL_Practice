import sqlite3


# Конектимся
db = sqlite3.connect('security.db')
cursor  = db.cursor()
# Создаём таблицу
cursor.execute('''CREATE TABLE IF NOT EXISTS staff (
               name TEXT NOT NULL,
               position TEXT)''')

cursor.execute('''INSERT INTO staff (name, position) VALUES ('Ivan', 'Admin')''')
cursor.execute('''INSERT INTO staff (name, position) VALUES ('Alex', 'Securite')''')

db.commit()
db.close()