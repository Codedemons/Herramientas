from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Reemplaza 'TU_TOKEN' con el token de tu bot proporcionado por BotFather
TOKEN = 'TU_TOKEN'

# Función para el comando /start
def start(update, context):
    update.message.reply_text('¡Hola! Soy un bot de ejemplo.')

# Función para el comando /ayuda
def help(update, context):
    update.message.reply_text('Puedes enviarme mensajes y te responderé.')

# Función para manejar mensajes recibidos
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Crea el objeto updater y pasa el token de tu bot
    updater = Updater(TOKEN, use_context=True)

    # Obtén el despachador para registrar los controladores
    dp = updater.dispatcher

    # Registra los controladores para los comandos
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Registra un controlador para manejar mensajes
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Inicia el bot
    updater.start_polling()

    # Detén el bot si se presiona Ctrl + C
    updater.idle()

if __name__ == '__main__':
    main()
