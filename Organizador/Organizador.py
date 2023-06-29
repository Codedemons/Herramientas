import os

def listar_directorio(directorio):
    archivos = os.listdir(directorio)
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        if os.path.isdir(ruta):
            print(f"Directorio: {ruta}")
        else:
            print(f"Archivo: {ruta}")

# Solicitar al usuario que ingrese un directorio
directorio_ingresado = input("Ingrese la ruta de un directorio: ")
# Llamar a la función para listar el contenido del directorio
listar_directorio(directorio_ingresado)
