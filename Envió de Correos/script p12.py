#LESSLIE MONTSERRAT MEDELLIN FLORES 1960113
#1960113

import smtplib, ssl
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = input("De: ")
receiver_email = input("Para: ")
password = getpass.getpass("Password: ")

#Informacion de asunto 
message = MIMEMultipart("alternative")
message["Subject"] = "Prueba de envio (script Python) - 1960113"
message["From"] = sender_email
message["To"] = receiver_email

#Se escribe el mensaje Html
html = """\
<html>
  <body>
    
    <p><strong> <h2> Practica 12 </h2> </strong> <br>
       Ejercicio de la practica 12 para envío de correos<br> 
       <strong> Alumno: </strong> Lesslie Medellin Flores <br>
       <strong> Matricula: </strong>  1960113
    </p>
  </body>
</html>
"""

#Se agrega al correo la parte del html 
parte_html = MIMEText(html, 'html')
message.attach(parte_html)

#Agregamos la imagen fcfm_cool.png
archivo = 'fcfm_cool.png'

#Abrimos el archivo 
with open(archivo, 'rb') as adjunto:
    contenido_adjunto = MIMEBase('application','octet-stream')
    contenido_adjunto.set_payload(adjunto.read())
encoders.encode_base64(contenido_adjunto)
contenido_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename= {archivo}"
)

#Agregamos al mensaje que enviaremos 
message.attach(contenido_adjunto)
mensaje_final = message.as_string()

#Conexion con smtp
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
