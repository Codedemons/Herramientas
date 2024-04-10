import tkinter as tk

class MiApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Mi Aplicación")
        self.geometry("400x300")

        # Crear widgets
        self.label = tk.Label(self, text="¡Bienvenido a mi aplicación!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Haz clic aquí", command=self.button_click)
        self.button.pack(pady=10)

    def button_click(self):
        # Función que se ejecuta cuando se hace clic en el botón
        self.label.config(text="¡Gracias por hacer clic!")

if __name__ == "__main__":
    app = MiApp()
    app.mainloop()
