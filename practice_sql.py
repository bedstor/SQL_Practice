# Импортируем модули
import sqlite3

# Создаем базу данных
db = sqlite3.connect('practice_base.db')
cursor = db.cursor()

# Создаем таблицу tasks
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               status TEXT)''')


title1, title2 = 'Купить хлеб', 'Написать код'
status = 'Новая'
# Добавляем в таблицу задачи
cursor.execute('''INSERT INTO tasks (title, status) VALUES (?, ?)''',
               (title1, status))

cursor.execute('''INSERT INTO tasks (title, status) VALUES (?, ?)''',
               (title2, status))

# Меняем статус одной задачи на выполено
cursor.execute('''UPDATE tasks SET status = "Выполнено" WHERE title = "Написать код"''')


# Удаляем из таблицы те задачи, которые выполнены
cursor.execute('''DELETE FROM tasks WHERE status = "Выполнено"''')

db.commit()
db.close()

# Этот коммит сделан через консоль Git!
