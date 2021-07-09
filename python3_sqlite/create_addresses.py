import sqlite3
conn = sqlite3.connect('addresses.db')

c = conn.cursor()

# Queries
# CREAR TABLAS: Se debe ejecutar solo una vez
# c.execute('''
#           CREATE TABLE person
#           (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
#           ''')
# c.execute('''
#           CREATE TABLE address
#           (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
#            post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
#            FOREIGN KEY(person_id) REFERENCES person(id))
#           ''')

### INSERTAR DATOS
# c.execute(''' 
#     INSERT INTO person VALUES(1, 'Javier')
# ''')
# c.execute(''' 
#     INSERT INTO person VALUES(2, 'Alejandra')
# ''')
# c.execute(''' 
#     INSERT INTO person VALUES(3, 'Matias')
# ''')
# c.execute('''
#     INSERT INTO person VALUES(4, 'Naty')
# ''')
# c.execute('''
#     INSERT INTO person VALUES(5, 'Victor');
# ''')
# c.execute('''
#     INSERT INTO address VALUES(1, 'Av. Medicos', '1', '00000', 1);
# ''')
# c.execute('''
#     INSERT INTO address VALUES(2, 'Centro', '1', '111', 2);
# ''')   
# c.execute('''
#     INSERT INTO address VALUES(3, 'Neuquén', '1', '222', 3);
# ''')
# c.execute('''
#     INSERT INTO address VALUES(4, 'Av. Brasil', '1', '333', 4);
# ''')
# c.execute('''
#     INSERT INTO address VALUES(5, 'Sanvi II', '1', '444', 5);
# ''')
# conn.commit()

### CONSULTAS
c.execute('SELECT * FROM person')
print(c.fetchall())
c.execute('SELECT * FROM address')
print(c.fetchall())

### CIERRE CONEXIÓN
conn.close()