import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def listar_archivos():
    directorio = filedialog.askdirectory()
    if directorio:
        archivos = os.listdir(directorio)
        for archivo in archivos:
            ruta = os.path.join(directorio, archivo)
            if os.path.isfile(ruta):
                nombre = archivo
                fecha_creacion = os.path.getctime(ruta)
                fecha_formateada = datetime.fromtimestamp(fecha_creacion).strftime("%d-%m-%y")
                lista_archivos.insert(tk.END, f"Nombre: {nombre}  |  Fecha de creación: {fecha_formateada}")

# Crear una ventana de Tkinter con resolución 640x360
ventana = tk.Tk()
ventana.geometry("640x360")
ventana.title("Organizador")

# Configurar el tamaño de las filas y columnas
ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)

# Crear el Listbox en la primera fila
lista_archivos = tk.Listbox(ventana, width=80)
lista_archivos.grid(row=0, column=0, sticky="nsew")

# Configurar el tamaño del Listbox para ocupar más espacio
lista_archivos.rowconfigure(0, weight=1)
lista_archivos.columnconfigure(0, weight=1)

# Crear el botón en la segunda fila y que ocupe la mitad del espacio del Listbox
boton = tk.Button(ventana, text="Seleccionar", command=listar_archivos)
boton.grid(row=1, column=0, sticky="nsew", padx=10, pady=10, ipady=30)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
