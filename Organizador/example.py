import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

# Crear una ventana de Tkinter
ventana = tk.Tk()
ventana.title("Estilo Clam para Listbox")

# Crear un estilo personalizado utilizando ttkthemes
style = ThemedStyle(ventana)
style.set_theme("clam")  # Seleccionar el tema "clam"

# Crear un Listbox con estilo
listbox = tk.Listbox(ventana, font=("Arial", 12), bg=style.lookup("TFrame", "background"),
                     fg=style.lookup("TFrame", "foreground"), selectbackground="gray",
                     selectforeground="white", relief="flat")
listbox.pack()

# Agregar elementos al Listbox
for i in range(1, 6):
    listbox.insert(tk.END, f"Elemento {i}")

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
