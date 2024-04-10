import pickle

# Datos a guardar en formato binario
datos = {
    'nombre': 'Juan',
    'edad': 30,
    'genero': 'Masculino'
}

# Guardar los datos en un archivo binario
with open('datos.bin', 'wb') as archivo_binario:
    pickle.dump(datos, archivo_binario)

# Leer los datos desde el archivo binario
with open('datos.bin', 'rb') as archivo_binario:
    datos_leidos = pickle.load(archivo_binario)

# Imprimir los datos leídos
print(datos_leidos)
