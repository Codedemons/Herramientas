import tkinter as tk
from tkinter import ttk

# Crear una ventana de Tkinter
ventana = tk.Tk()
ventana.geometry("640x360")
ventana.title("Mejor Presentación")

# Crear un estilo utilizando el módulo ttk
style = ttk.Style(ventana)

# Establecer un tema para el estilo (opcional)
style.theme_use("clam")

# Configurar el estilo para los botones
style.configure("TButton", font=("Arial", 12), padding=10)

# Configurar el estilo para los títulos
style.configure("TLabel", font=("Arial", 14, "bold"), padding=10)

# Crear etiquetas con estilo
etiqueta_titulo = ttk.Label(ventana, text="Bienvenido", style="TLabel")
etiqueta_titulo.pack()

etiqueta_descripcion = ttk.Label(ventana, text="Esto es un ejemplo de mejor presentación", style="TLabel")
etiqueta_descripcion.pack()

# Crear botones con estilo
boton_1 = ttk.Button(ventana, text="Botón 1", style="TButton")
boton_1.pack()

boton_2 = ttk.Button(ventana, text="Botón 2", style="TButton")
boton_2.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
