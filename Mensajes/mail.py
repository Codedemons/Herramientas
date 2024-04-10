import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurar los detalles del correo electrónico
sender_email = "codedemonscm@gmail.com"
receiver_email = "puch.infy@gmail.com"
password = "keys"
subject = "Asunto del correo"
message = "Cuerpo del correo electrónico."

# Crear el objeto MIMEMultipart
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Agregar el cuerpo del correo electrónico
msg.attach(MIMEText(message, 'plain'))

# Iniciar una conexión SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Iniciar sesión en el servidor SMTP
server.login(sender_email, password)

# Enviar el correo electrónico
server.sendmail(sender_email, receiver_email, msg.as_string())

# Cerrar la conexión SMTP
server.quit()

print("¡Correo electrónico enviado correctamente!")
