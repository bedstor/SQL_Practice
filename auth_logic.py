# Импортируем все нужные библиотеки
import sqlite3


# Создаем базу данных
db = sqlite3.connect('system.db')
cursor = db.cursor()


# Создаем базу users
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               name VARCHAR(30) UNIQUE,
               visits INTEGER DEFAULT 1)'''
)


# Спрашиваме имя у пользователя
name_ans = input('Введите имя\n')


# Проверяем имя и записываем в переменную
cursor.execut("SELECT visits FROM users WHERE name = ?", (name_ans,))
user_data = cursor.fetchone()


# Обрабатываем значение
if user_data == None:
    cursor.execute('''INSERT INTO users (name) VALUES (?)''', (name_ans,))
    print(f'Привет, {name_ans}! Я тебя запомнил')
else:
    current_visits = int(user_data[0]) + 1
    cursor.execute('''UPDATE users SET visits = ? WHERE name = ?''', (current_visits, name_ans))
    print(f'О, привет! Это твой {current_visits} раз')


db.commit()
db.close()
