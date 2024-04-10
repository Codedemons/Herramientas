import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os


def center_window(window, width, height):
    """Centra la ventana en la pantalla."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x_coordinate, y_coordinate))


def mostrar_contenido_carpeta():
    # Obtener la ruta de la carpeta seleccionada por el usuario
    carpeta_seleccionada = filedialog.askdirectory()
    
    # Verificar si se seleccionó una carpeta
    if carpeta_seleccionada:
        # Ocultar el botón
        boton_seleccionar_carpeta.pack_forget()
        
        # Obtener la lista de archivos y carpetas dentro de la carpeta
        contenido_carpeta = os.listdir(carpeta_seleccionada)
        
        # Insertar datos en el Treeview
        for item in contenido_carpeta:
            treeview.insert('', 'end', values=(item, os.path.join(carpeta_seleccionada, item)))
        
        # Mostrar el Treeview
        treeview.pack(padx=10, pady=10, fill='both', expand=True)


# Crear una ventana
ventana = tk.Tk()
ventana.title("Tabla de Contenidos")

# Configurar el estilo de los widgets de ttk
style = ttk.Style()
style.theme_use('clam')  # Puedes cambiar 'clam' por otros estilos disponibles


# Configurar el tamaño de la ventana y centrarla en la pantalla
ancho_ventana = 800
alto_ventana = 600
ventana.geometry('{}x{}'.format(ancho_ventana, alto_ventana))
center_window(ventana, ancho_ventana, alto_ventana)

# Configurar estilo del botón
style.configure('Boton.TButton', font=('Helvetica', 12), background='#4CAF50', foreground='white', padding=60)

# Crear un botón para seleccionar la carpeta y posicionarlo a la izquierda con tamaño 200x200
boton_seleccionar_carpeta = ttk.Button(ventana, text="Seleccionar Carpeta", command=mostrar_contenido_carpeta, style='Boton.TButton')
boton_seleccionar_carpeta.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)


# Crear un Treeview para mostrar el contenido de la carpeta
treeview = ttk.Treeview(ventana, columns=('Nombre', 'Ruta'), show='headings')
treeview.heading('Nombre', text='Nombre del Archivo')
treeview.heading('Ruta', text='Ruta del Archivo')

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
