import csv

# Leer el archivo CSV
with open('datos.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    
    # Iterar sobre cada fila del archivo CSV
    for fila in lector_csv:
        print(fila)  # Imprimir cada fila

# Escribir en un archivo CSV
datos = [
    ['Pedro', 35, 'Masculino'],
    ['Ana', 28, 'Femenino']
]

with open('nuevos_datos.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir cada fila en el archivo CSV
    for fila in datos:
        escritor_csv.writerow(fila)

print("Datos escritos en nuevos_datos.csv.")
