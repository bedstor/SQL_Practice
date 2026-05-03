# Импортируем библиотеки
import sqlite3


# Создаем базу
db = sqlite3.connect('shop_base.db')
cursor = db.cursor()

# Создаём таблицу
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               price INTEGER,
               stock INTEGER)''')

# Добавляем товары
cursor.execute('''INSERT INTO products(name, price, stock) VALUES (?, ?, ?)''', ("Gems", 500, 10))
cursor.execute('''INSERT INTO products(name, price, stock) VALUES (?, ?, ?)''', ("Skin", 1000, 5))
cursor.execute('''INSERT INTO products(name, price, stock) VALUES (?, ?, ?)''', ("Box", 200, 20))


# Обновляем данные
cursor.execute('''UPDATE products SET price = 800, stock = 4 WHERE name = "Skin"''')


# Выводим товары, которые дешевле 900 рублей
cursor.execute('''SELECT name FROM products WHERE price < 900 AND stock > 0''')
results = cursor.fetchall()
print(results)


# Удаляем товар box
cursor.execute('''DELETE FROM products WHERE name = "Box"''')

db.commit()
db.close()