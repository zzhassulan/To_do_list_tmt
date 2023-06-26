import sqlite3

# Создание таблицы для задач
def create_tasks_table():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  description TEXT NOT NULL,
                  status TEXT NOT NULL)''')
    conn.commit()
    conn.close()