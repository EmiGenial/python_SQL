import sqlite3
conn = sqlite3.connect('db/sqlite.db')

c = conn.cursor()

### CONSULTAS
print('SALARIOS')
# c.execute('SELECT * FROM empleados')
c.execute('SELECT nombre, sueldobasico from empleados WHERE sueldobasico > 650')
for empleado in c.fetchall():
    print(empleado)

print('')
print('LIBROS DE BORGES:')
c.execute(''' select * from libros where autor='Borges' ''')
for libro in c.fetchall():
    print(libro)

print('')
print('EDITORIAL: Emece')
c.execute(''' select titulo from libros where editorial='Emece' ''')
for libro in c.fetchall():
    print(libro)

### CIERRE CONEXIÓN
conn.close()