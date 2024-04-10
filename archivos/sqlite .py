import sqlite3

# Conexión a la base de datos (se crea si no existe)
conexion = sqlite3.connect('ejemplo.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER, ciudad TEXT)''')

# Insertar datos en la tabla
cursor.execute("INSERT INTO usuarios (nombre, edad, ciudad) VALUES (?, ?, ?)", ('Juan', 30, 'Madrid'))
cursor.execute("INSERT INTO usuarios (nombre, edad, ciudad) VALUES (?, ?, ?)", ('María', 25, 'Barcelona'))

# Guardar (commit) los cambios
conexion.commit()

# Consultar datos
cursor.execute("SELECT * FROM usuarios")
filas = cursor.fetchall()

# Imprimir los resultados
for fila in filas:
    print(fila)

# Cerrar la conexión
conexion.close()
