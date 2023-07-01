
import os
import tkinter as tk
from tkinter import ttk
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

        for fecha in fechas:
            carpeta_fecha = os.path.join(carpeta_procesamiento, fecha)
            if not os.path.exists(carpeta_fecha):
                os.mkdir(carpeta_fecha)

            # Crear las subcarpetas "Imagenes", "Videos" y "Otros" dentro de la carpeta de fecha
            carpeta_imagenes = os.path.join(carpeta_fecha, "Imagenes")
            carpeta_videos = os.path.join(carpeta_fecha, "Videos")
            carpeta_otros = os.path.join(carpeta_fecha, "Otros")
            os.mkdir(carpeta_imagenes)
            os.mkdir(carpeta_videos)
            os.mkdir(carpeta_otros)

        # Mover los archivos a las carpetas correspondientes
        for archivo in archivos:
            ruta = archivo['ruta']
            nombre = archivo['nombre']
            fecha_creacion = archivo['fecha_creacion']
            fecha_formateada = datetime.fromtimestamp(fecha_creacion).strftime("%d-%m-%y")
            carpeta_destino = os.path.join(carpeta_procesamiento, fecha_formateada)
            extension = os.path.splitext(nombre)[1][1:].lower()
            if extension in ["jpg", "png", "gif"]:
                carpeta_destino = os.path.join(carpeta_destino, "Imagenes")
            elif extension in ["mp4", "avi", "mkv"]:
                carpeta_destino = os.path.join(carpeta_destino, "Videos")
            else:
                carpeta_destino = os.path.join(carpeta_destino, "Otros")
            ruta_destino = os.path.join(carpeta_destino, nombre)
            os.rename(ruta, ruta_destino)

        lista_archivos.delete(0, tk.END)  # Limpiar la lista de archivos
        lista_archivos.insert(tk.END, "Archivos movidos correctamente.")

# Crear una ventana de Tkinter con resolución 640x360
ventana = tk.Tk()
ventana.geometry("640x360")
ventana.title("Organizador")
#Canbia el icono de la ventana
icono = tk.PhotoImage(file="Organizador/lista.png")
ventana.iconphoto(True,icono)

# Create a style using the ttk module
style = ttk.Style(ventana)

# Set a theme for the style (optional)
style.theme_use("clam")

# Configure the style for buttons
style.configure("TButton", font=("Arial", 12), padding=10)

# Configure the style for labels
style.configure("TLabel", font=("Arial", 14, "bold"), padding=10)

# Configurar el tamaño de las filas y columnas
ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)

# Crear el Listbox en la primera fila
lista_archivos = tk.Listbox(ventana, font=("Arial", 10), bg=style.lookup("TFrame", "background"),
                     fg=style.lookup("TFrame", "foreground"), selectbackground="gray",
                     selectforeground="white", relief="flat")
lista_archivos.grid(row=0, column=0, rowspan=4, sticky="nsew")

# Configurar el tamaño del Listbox para ocupar más espacio
lista_archivos.rowconfigure(0, weight=1)
lista_archivos.columnconfigure(0, weight=1)

# Crear el botón "Seleccionar" en la segunda fila
boton_seleccionar = ttk.Button(ventana, text="Seleccionar", style="TButton",command=listar_archivos)
boton_seleccionar.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

# Crear el botón "Crear Carpetas" en la tercera fila
boton_crear_carpetas = ttk.Button(ventana, text="Crear Carpetas", style="TButton",command=crear_carpetas)
boton_crear_carpetas.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
