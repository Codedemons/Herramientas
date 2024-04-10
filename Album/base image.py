import os
import tkinter as tk

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Archivos")

        # Definir el tamaño de la ventana
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

        # Obtener la ubicación del script y la imagen
        script_dir = os.path.dirname(__file__)
        image_path = os.path.join(script_dir, "carpeta.png")

        # Cargar la imagen y redimensionarla a 600x400
        original_image = tk.PhotoImage(file=image_path)
        self.image = original_image.subsample(original_image.width() // 600, original_image.height() // 400)

        # Mostrar la imagen en un widget Label
        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
