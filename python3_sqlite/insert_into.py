import sqlite3
conn = sqlite3.connect('db/sqlite.db')

c = conn.cursor()

# INSERT Usuarios
c.execute(''' insert into usuarios (nombre, clave) values ('MarioPerez','Marito14') ''')
c.execute(''' insert into usuarios (nombre, clave) values ('MariaGarcia','Mary88') ''')
c.execute(''' insert into usuarios (nombre, clave) values ('DiegoRodriguez','z8080') ''')

# INSERT Empleados
c.execute('''
    insert into empleados (nombre, documento, sexo, domicilio, sueldobasico)
    values ('Juan Perez',22333444,'m','Sarmiento 123',500.25) 
''')
c.execute('''
    insert into empleados (nombre, documento, sexo, domicilio, sueldobasico)
    values ('Ana Acosta',24555666,'f','Colon 134',650)
''')
c.execute('''
    insert into empleados (nombre, documento, sexo, domicilio, sueldobasico)
    values ('Bartolome Barrios',27888999,'m','Urquiza 479',800)   
''')
c.execute('''
    insert into empleados (nombre, documento, sexo, domicilio, sueldobasico)
    values ('Carlos Rodriguez',55522211,'m','Urquiza 784',900)   
''')

# INSERT Libros
c.execute('''
insert into libros(titulo,autor,editorial,precio,cantidad) 
values('El aleph','Borges','Emece',100,3)
''')
c.execute('''
 insert into libros(titulo,autor,editorial,precio,cantidad) 
 values('Martin Fierro','Jose Hernandez','Emece',67,44)
''')
c.execute('''
 insert into libros(titulo,autor,editorial,precio,cantidad)
 values('Martin Fierro','Jose Hernandez','Planeta',250.30,2) 
''')
c.execute('''
  insert into libros(titulo,autor,editorial,precio,cantidad)
  values('Aprenda PHP','Mario Molina','Siglo XXI',120,1)
''')

# INSERT Articulos
c.execute('''
  insert into articulos (codigo, nombre, descripcion, precio,cantidad)
  values (1,'impresora', 'MULTIFUNCION HP 2135', 1800, 10);
''')

c.execute('''
  insert into articulos (codigo, nombre, descripcion, precio,cantidad)
  values (2,'impresora', 'MULTIFUNCION EPSON EXPRESSION XP241 WI-FI', 2500, 30);
''')

c.execute('''
  insert into articulos (codigo, nombre, descripcion, precio,cantidad)
  values (3,'monitor', 'Samsung 23', 1200, 10);
''')

c.execute('''
  insert into articulos (codigo, nombre, descripcion, precio,cantidad)
  values (4,'teclado', 'ingles Biswal', 100, 50);
''')

c.execute('''
  insert into articulos (codigo, nombre, descripcion, precio,cantidad)
  values (5,'teclado', 'español Biswal', 90, 50);
''')

c.execute('''
  insert into articulos (codigo, nombre, descripcion, precio,cantidad)
  values (6,'Audífonos', 'Beats Audio', 400, 72);
''')

conn.commit()

### CIERRE CONEXIÓN
conn.close()