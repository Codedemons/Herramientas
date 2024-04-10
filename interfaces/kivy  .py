import kivy
from kivy.app import App
from kivy.uix.button import Button

# Configuración de Kivy
kivy.require('2.0.0')  # Requerimos Kivy versión 2.0.0 o superior

class MiApp(App):
    def build(self):
        # Creamos un botón
        btn = Button(text='¡Hola, Kivy!')

        # Registramos una función para que se ejecute cuando se haga clic en el botón
        btn.bind(on_press=self.on_button_click)

        return btn

    def on_button_click(self, instance):
        # Esta función se ejecutará cuando se haga clic en el botón
        print('¡Se ha hecho clic en el botón!')

# Ejecutamos la aplicación
if __name__ == '__main__':
    MiApp().run()
