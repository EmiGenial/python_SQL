import sqlite3
conn = sqlite3.connect('db/sqlite.db')

c = conn.cursor()

c.execute(''' drop table if exists usuarios; ''')
c.execute(''' drop table if exists libros; ''')
c.execute(''' drop table if exists empleados; ''')
c.execute(''' drop table if exists articulos; ''')

c.execute(''' create table usuarios (nombre text, clave text) ''')

c.execute(''' create table libros( 
    titulo text,
    autor text,
    editorial text,
    precio real,
    cantidad integer
 );
''')

c.execute('''
create table empleados (
	nombre text,
	documento integer,
	sexo text,
	domicilio text,
	sueldobasico real
)
''')

c.execute('''
create table articulos (
	codigo integer,
	nombre text,
	descripcion text,
	precio real,
	cantidad integer
);
''')

conn.close()