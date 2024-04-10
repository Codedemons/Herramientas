import simplejson as json

# Datos a guardar en el archivo JSON
datos = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 30,
    "ciudad": "Ejemplo City"
}

# Nombre del archivo donde se guardarán los datos
nombre_archivo = "datos.json"

# Guardar los datos en el archivo JSON
with open(nombre_archivo, "w") as archivo:
    json.dump(datos, archivo)

print("Datos guardados exitosamente en el archivo:", nombre_archivo)
