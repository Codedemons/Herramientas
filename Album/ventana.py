import tkinter as tk

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Archivos")
        self.root.geometry("600x400")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
