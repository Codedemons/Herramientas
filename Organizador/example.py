import os
import tkinter as tk
from tkinter import filedialog

def listar_archivos():
    directorio = filedialog.askdirectory()
    if directorio:
        archivos = os.listdir(directorio)
        for archivo in archivos:
            ruta = os.path.join(directorio, archivo)
            if os.path.isfile(ruta):
                lista_archivos.insert(tk.END, f"Archivo: {ruta}")

# Crear una ventana de Tkinter con resolución 640x360
ventana = tk.Tk()
ventana.geometry("640x360")
ventana.title("Organizador")

# Configurar el tamaño de las filas y columnas
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)

# Crear el botón en la primera fila
boton = tk.Button(ventana, text="Seleccionar directorio", command=listar_archivos)
boton.grid(row=0, column=0, sticky="nsew")

# Crear el Listbox en la segunda fila
lista_archivos = tk.Listbox(ventana)
lista_archivos.grid(row=1, column=0, sticky="nsew")

# Configurar el tamaño del Listbox para ocupar más espacio
lista_archivos.rowconfigure(0, weight=1)
lista_archivos.columnconfigure(0, weight=1)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
