import sqlite3


# Подключаемся к базе
db = sqlite3.connect('security.db')
cursor = db.cursor()
# Удаляем старую таблицу
cursor.execute('''DROP TABLE IF EXISTS staff''')
# Создаём новую таблицу 
cursor.execute('''CREATE TABLE IF NOT EXISTS staff(
               name TEXT NOT NULL,
               position TEXT,
               entry_count INT)''')


cursor.execute('''INSERT INTO staff (name, position, entry_count) VALUES ("Ivan", "Admin", 10)''')
cursor.execute("INSERT INTO staff (name, position, entry_count) VALUES ('Alex', 'Security', 5)")

# Достаём из базы только тех, у кого входов больше 7
cursor.execute("SELECT * FROM staff WHERE entry_count > 7")
# Записываем в перменнную
results = cursor.fetchall()
# Выводим 
print(results)


db.commit()
db.close()