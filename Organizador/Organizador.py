import os
import tkinter as tk
from tkinter import filedialog

def listar_directorio():
    directorio = filedialog.askdirectory()
    if directorio:
        archivos = os.listdir(directorio)
        for archivo in archivos:
            ruta = os.path.join(directorio, archivo)
            if os.path.isdir(ruta):
                lista_directorios.insert(tk.END, f"Directorio: {ruta}")
            else:
                lista_directorios.insert(tk.END, f"Archivo: {ruta}")

# Crear una ventana de Tkinter con resolución 640x360
ventana = tk.Tk()
ventana.geometry("640x360")
ventana.title("Organizador")

# Configurar el tamaño de las filas y columnas
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

# Crear el botón en la primera columna y abarcar 2 filas en posición vertical
boton = tk.Button(ventana, text="Seleccionar directorio", command=listar_directorio)
boton.grid(row=1, column=0, rowspan=2, sticky="nsew")

# Crear el Listbox en la segunda columna
lista_directorios = tk.Listbox(ventana)
lista_directorios.grid(row=1, column=1, rowspan=2, sticky="nsew")

# Configurar el tamaño del Listbox para ocupar más espacio
lista_directorios.rowconfigure(0, weight=1)
lista_directorios.columnconfigure(0, weight=1)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
