import wx

class MiVentana(wx.Frame):
    def __init__(self, *args, **kw):
        super(MiVentana, self).__init__(*args, **kw)

        # Configuramos el título de la ventana
        self.SetTitle('Mi Aplicación con wxPython')

        # Creamos un panel para contener los widgets
        panel = wx.Panel(self)

        # Creamos un botón en el panel
        self.btn = wx.Button(panel, label='Haz clic aquí')

        # Bind del evento de clic del botón
        self.btn.Bind(wx.EVT_BUTTON, self.on_button_click)

        # Creamos un layout vertical
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.btn, 0, wx.ALL|wx.CENTER, 10)

        # Asignamos el layout al panel
        panel.SetSizer(sizer)

        # Ajustamos el tamaño de la ventana automáticamente
        self.Fit()

    def on_button_click(self, event):
        # Esta función se ejecuta cuando se hace clic en el botón
        wx.MessageBox('¡Hola, wxPython!')

if __name__ == '__main__':
    app = wx.App(False)
    frame = MiVentana(None)
    frame.Show(True)
    app.MainLoop()
