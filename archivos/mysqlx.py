import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hms"
    )
    print('funcionando')
except mysql.connector.Error as error:
    print("Error al conectar a la base de datos:", error)
