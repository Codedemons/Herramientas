import tkinter as tk
from tkinter import ttk

# Create a Tkinter window
ventana = tk.Tk()
ventana.title("Mejor Presentación")

# Create a style using the ttk module
style = ttk.Style(ventana)

# Set a theme for the style (optional)
style.theme_use("clam")

# Configure the style for buttons
style.configure("TButton", font=("Arial", 12), padding=10)

# Configure the style for labels
style.configure("TLabel", font=("Arial", 14, "bold"), padding=10)

# Create labels with style
etiqueta_titulo = ttk.Label(ventana, text="Bienvenido", style="TLabel")
etiqueta_titulo.grid(row=0, column=0)

etiqueta_descripcion = ttk.Label(ventana, text="Esto es un ejemplo de mejor presentación", style="TLabel")
etiqueta_descripcion.grid(row=1, column=0)

# Create buttons with style
boton_1 = ttk.Button(ventana, text="Botón 1", style="TButton")
boton_1.grid(row=2, column=0, pady=10)

boton_2 = ttk.Button(ventana, text="Botón 2", style="TButton")
boton_2.grid(row=3, column=0, pady=10)

# Run the main event loop
ventana.mainloop()
