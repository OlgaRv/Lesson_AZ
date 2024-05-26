import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL)
 ''')
cur.execute('INSERT INTO users VALUES (?, ?, ?)', (1, "John", 25))
cur.execute('INSERT INTO users VALUES (?, ?, ?)', (2, "Anna", 30))

conn.commit()
conn.close()



