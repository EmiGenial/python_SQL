import sqlite3
conn = sqlite3.connect('db/sqlite.db')

c = conn.cursor()

# Elimine los artículos cuyo precio sea mayor o igual a 500
c.execute(''' DELETE FROM articulos WHERE precio>=500; ''')

# Elimine todas las impresoras
c.execute(''' DELETE from articulos where nombre='impresora'; ''')

# Elimine todos los artículos cuyo código sea diferente a 4
c.execute(''' DELETE from articulos where codigo<>4 ''')

conn.commit()

### CIERRE CONEXIÓN
conn.close()