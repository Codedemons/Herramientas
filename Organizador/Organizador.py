import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

directorio_seleccionado = ""

def listar_archivos():
    global directorio_seleccionado
    directorio_seleccionado = filedialog.askdirectory()
    if directorio_seleccionado:
        archivos = obtener_archivos(directorio_seleccionado)
        for archivo in archivos:
            ruta = archivo['ruta']
            nombre = archivo['nombre']
            fecha_creacion = archivo['fecha_creacion']
            fecha_formateada = datetime.fromtimestamp(fecha_creacion).strftime("%d-%m-%y")
            lista_archivos.insert(tk.END, f"Nombre: {nombre}  |  Fecha de creación: {fecha_formateada}")

def obtener_archivos(directorio):
    archivos = []
    for ruta_padre, carpetas, archivos_en_carpeta in os.walk(directorio):
        for archivo in archivos_en_carpeta:
            ruta_completa = os.path.join(ruta_padre, archivo)
            if os.path.isfile(ruta_completa):
                fecha_creacion = os.path.getctime(ruta_completa)
                archivos.append({
                    'ruta': ruta_completa,
                    'nombre': archivo,
                    'fecha_creacion': fecha_creacion
                })
    return archivos

def crear_carpetas():
    global directorio_seleccionado
    if directorio_seleccionado:
        archivos = obtener_archivos(directorio_seleccionado)
        fechas = set()  # Conjunto para almacenar las fechas únicas
        for archivo in archivos:
            fecha_creacion = archivo['fecha_creacion']
            fecha_formateada = datetime.fromtimestamp(fecha_creacion).strftime("%d-%m-%y")
            fechas.add(fecha_formateada)

        # Crear la carpeta "procesamiento" si no existe
        carpeta_procesamiento = os.path.join(directorio_seleccionado, "procesamiento")
        if not os.path.exists(carpeta_procesamiento):
            os.mkdir(carpeta_procesamiento)

        # Crear las subcarpetas para las fechas únicas
        for fecha in fechas:
            carpeta_fecha = os.path.join(carpeta_procesamiento, fecha)
            if not os.path.exists(carpeta_fecha):
                os.mkdir(carpeta_fecha)

# Crear una ventana de Tkinter con resolución 640x360
ventana = tk.Tk()
ventana.geometry("640x360")
ventana.title("Organizador")

# Configurar el tamaño de las filas y columnas
ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)

# Crear el Listbox en la primera fila
lista_archivos = tk.Listbox(ventana, width=80)
lista_archivos.grid(row=0, column=0, rowspan=4, sticky="nsew")

# Configurar el tamaño del Listbox para ocupar más espacio
lista_archivos.rowconfigure(0, weight=1)
lista_archivos.columnconfigure(0, weight=1)

# Crear el botón "Seleccionar" en la segunda fila
boton_seleccionar = tk.Button(ventana, text="Seleccionar", command=listar_archivos)
boton_seleccionar.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

# Crear el botón "Crear Carpetas" en la tercera fila
boton_crear_carpetas = tk.Button(ventana, text="Crear Carpetas", command=crear_carpetas)
boton_crear_carpetas.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
