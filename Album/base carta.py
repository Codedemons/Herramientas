import tkinter as tk
from tkinter import ttk
import os

class WindowConfigurator:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Archivos")
        
        window_width = 800
        window_height = 600
        
        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular las coordenadas de la esquina superior izquierda de la ventana
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        # Definir el tamaño y la posición de la ventana
        self.root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_coordinate, y_coordinate))

        self.root.style = ttk.Style()
        self.root.style.configure("Outer.TFrame", background="#CCCCCC", bordercolor="#CCCCCC", borderwidth=5, relief=tk.SOLID)


class WidgetManager:
    def __init__(self, root):
        self.root = root

        self.outer_frame = ttk.Frame(root, style="Outer.TFrame")
        self.outer_frame.place(x=20, y=20)  # Cambia aquí: posicionar el outer_frame en (20, 20)

        self.inner_frame = ttk.Frame(self.outer_frame, style="Inner.TFrame")
        self.inner_frame.pack(padx=20, pady=20)

        script_dir = os.path.dirname(__file__)
        image_path = os.path.join(script_dir, "carpeta.png")
        original_image = tk.PhotoImage(file=image_path)
        self.image = original_image.subsample(original_image.width() // 200, original_image.height() // 150)

        self.image_label = tk.Label(self.inner_frame, image=self.image, bg="#F0F0F0")
        self.image_label.pack(pady=20)

        
        self.title_label = tk.Label(self.inner_frame, text="Título de la imagen", font=("Arial", 20), bg="#F0F0F0", fg="#333333")
        self.title_label.pack()

        self.subtitle_label = tk.Label(self.inner_frame, text="Subtítulo de la imagen", font=("Arial", 14), bg="#F0F0F0", fg="#666666")
        self.subtitle_label.pack()



if __name__ == "__main__":
    root = tk.Tk()
    
    window_configurator = WindowConfigurator(root)
    widget_manager = WidgetManager(root)
    
    root.mainloop()
