import sqlite3

conn = sqlite3.connect('dbq.sql')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                amount INTEGER DEFAULT 0
            )''')

conn.commit()
cur.close()
conn.close()

print("Database is created!")
