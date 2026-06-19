import sqlite3

conn = sqlite3.connect('buspass.db')

cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS buspass(
id INTEGER PRIMARY KEY,
name TEXT,
source TEXT,
destination TEXT,
price REAL,
passid TEXT
)
''')

conn.commit()
conn.close()

print("Database Created")