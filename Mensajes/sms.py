import requests

# Detalles del mensaje
from_number = '9381683766'
to_number = '9381236756'
message_body = 'Hola, este es un mensaje de prueba enviado mediante TextBelt SMS.'

# URL de la API de TextBelt
url = 'https://textbelt.com/text'

# Parámetros del mensaje
params = {
    'phone': to_number,
    'message': message_body,
    'key': 'textbelt',  # Usando la clave predeterminada para mensajes gratuitos
}

# Enviar el mensaje
response = requests.post(url, params=params)

# Verificar la respuesta
if response.status_code == 200:
    print("Mensaje enviado exitosamente.")
else:
    print("Error al enviar el mensaje:", response.text)
