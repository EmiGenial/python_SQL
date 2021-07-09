import sqlite3
conn = sqlite3.connect('db/sqlite.db')

c = conn.cursor()

c.execute('''

''')

conn.commit()

### CIERRE CONEXIÓN
conn.close()