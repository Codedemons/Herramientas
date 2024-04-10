from telegram import Bot
import requests

# Reemplaza 'TOKEN' con el token de tu bot proporcionado por BotFather
TOKEN = '7168261033:AAGZIX9y0T_RjCkfo0qMoj1n6C96Gt6TAEk'

# Reemplaza 'CHAT_ID' con el ID del chat al que deseas enviar el mensaje
CHAT_ID = '1456899513'


def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    datos = {
        "chat_id": CHAT_ID,
        "text": texto
    }
    response = requests.post(url, data=datos)
    if response.status_code == 200:
        print("Mensaje enviado exitosamente.")
    else:
        print("Error al enviar el mensaje:", response.text)

if __name__ == "__main__":
    mensaje = "Hola, este es otro mensaje enviado desde Python utilizando Telegram."
    enviar_mensaje(mensaje)
