import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def center_window(window, width, height):
    """Centra la ventana en la pantalla."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x_coordinate, y_coordinate))

def mostrar_album_carpeta():
    # Obtener la ruta de la carpeta seleccionada por el usuario
    carpeta_seleccionada = filedialog.askdirectory()
    
    # Verificar si se seleccionó una carpeta
    if carpeta_seleccionada:
        # Ocultar el botón
        boton_seleccionar_carpeta.pack_forget()
        
        # Obtener la lista de archivos y carpetas dentro de la carpeta
        contenido_carpeta = os.listdir(carpeta_seleccionada)
        
        # Mostrar todos los elementos (archivos y carpetas) en el álbum
        mostrar_carpetas(carpeta_seleccionada, contenido_carpeta)

def mostrar_carpetas(carpeta_padre, subcarpetas):
    # Crear un lienzo (Canvas) y eliminar el margen blanco
    canvas = tk.Canvas(ventana, bg='#093573', highlightthickness=0, highlightbackground='#f0f0f0')
    canvas.pack(fill=tk.BOTH, expand=True)

    # Calcular el número de columnas y filas para el álbum de carpetas
    columnas = 4

    # Iterar sobre las subcarpetas y mostrar miniaturas de carpetas
    for i, nombre_carpeta in enumerate(subcarpetas):
        ruta_completa = os.path.join(carpeta_padre, nombre_carpeta)

        columna = i % columnas
        fila = i // columnas

        # Crear un botón para representar la carpeta y aplicar el nuevo estilo
        boton_carpeta = ttk.Button(canvas, text=nombre_carpeta, command=lambda ruta=ruta_completa: abrir_carpeta(ruta), style='BotonCarpeta.TButton')
        boton_carpeta.grid(row=fila, column=columna, padx=10, pady=10)

        # Obtener la ruta de la imagen y cargarla
        ruta_imagen = os.path.join(carpeta_padre, nombre_carpeta, "carpeta.png")  # Cambia "imagen.jpg" por el nombre de tu imagen
        if os.path.exists(ruta_imagen):
            imagen_original = Image.open(ruta_imagen)
            imagen_redimensionada = resize_image(imagen_original, 100, 100)  # Ajusta el tamaño de la imagen según sea necesario
            imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
            etiqueta_imagen = tk.Label(canvas, image=imagen_tk)
            etiqueta_imagen.grid(row=fila + 1, column=columna, padx=10, pady=5)  # Colocar la imagen debajo del botón

            # Asegurarse de que la imagen no sea eliminada por el recolector de basura
            etiqueta_imagen.image = imagen_tk

def abrir_carpeta(ruta):
    # Abre la carpeta seleccionada
    os.startfile(ruta)


def resize_image(imagen, width, height):
    """Redimensiona una imagen al ancho y alto especificados."""
    return imagen.resize((width, height), Image.LANCZOS)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Álbum de Carpetas")

# Cambiar el color de fondo de la ventana
ventana.configure(bg='#093573')  # Puedes cambiar '#f0f0f0' por cualquier otro color hexadecimal

# Configurar el estilo de los widgets de ttk
style = ttk.Style()
style.theme_use('clam')  # Puedes cambiar 'clam' por otros estilos disponibles



# Configurar el tamaño de la ventana y centrarla en la pantalla
ancho_ventana = 800
alto_ventana = 600
ventana.geometry('{}x{}'.format(ancho_ventana, alto_ventana))
center_window(ventana, ancho_ventana, alto_ventana)

# Ejecutar el bu# Configurar estilo del botón
#style.configure('Boton.TButton', font=('Helvetica', 12), background='#4CAF50', foreground='white', padding=60)
#Crear un botón para seleccionar la carpeta y posicionarlo a la izquierda con tamaño 200x200
#boton_seleccionar_carpeta = ttk.Button(ventana, text="Seleccionar Carpeta", command=mostrar_album_carpeta, style='Boton.TButton')
#boton_seleccionar_carpeta.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)

# Obtener la ruta de la imagen y cargarla
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(directorio_actual, "src", "img", "carpeta.png")
imagen_original = Image.open(ruta_imagen)
# Redimensionar la imagen al tamaño deseado
imagen_redimensionada = resize_image(imagen_original, 130, 100)
# Convertir la imagen redimensionada a un objeto PhotoImage
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
# Crear un estilo personalizado
style = ttk.Style()

# Configurar el color de fondo del botón
style.configure('Custom.TButton', background='#FF5733')  # Cambia '#FF5733' por el color deseado en formato hexadecimal

# Crear un botón para seleccionar la carpeta y posicionarlo a la izquierda con la imagen
boton_seleccionar_carpeta = ttk.Button(ventana, image=imagen_tk, command=mostrar_album_carpeta, style='Custom.TButton')
boton_seleccionar_carpeta.pack(side=tk.TOP, padx=20, pady=20, anchor=tk.NW)


# Configurar estilo del botón de carpetas
style.configure('BotonCarpeta.TButton', font=('Helvetica', 12), background='#2196F3', foreground='black', padding=30)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
