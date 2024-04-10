# Datos a escribir en el archivo de texto
datos = [
    "Línea 1",
    "Línea 2",
    "Línea 3"
]

# Ruta del archivo de texto
ruta_archivo = "datos.txt"

# Escribir en el archivo de texto
with open(ruta_archivo, "w") as archivo:
    for linea in datos:
        archivo.write(linea + "\n")
