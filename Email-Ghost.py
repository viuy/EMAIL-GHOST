import smtplib
import os
import sys
suma = 1
numero = 1
class color:
    GREEN = "\033[92m"
    RESET = "\033[0m"
    yellow = "\033[93m"
    cyan = "\033[36m"

print(" ")
print(color.yellow + "EMAIL-GHOST")
print(" ")
print(color.yellow + "by VIUY" )
print(color.cyan + "TikTok: viuy.tt" )
print("instagram: viuy_ig")
print(" ")
print(color.GREEN + "bienvenido,para usar este script entra a:")
print("https://myaccount.google.com/lesssecureapps y permite el acceso de aplicacioes poco seguras")
print("(con la cuenta con la que vayas a spamear).")
print(" ")

tucorreo = input("¿con que correo quieres espamear?" + color.RESET + "")
contraseña = input(color.GREEN + "¿cual es la contraseña del correo?" + color.RESET + "")
correo = input(color.GREEN + "¿a que correo quieres espamear?" + color.RESET + "")
mensaje = input(color.GREEN + "¿que mensaje quieres espamear?" + color.RESET + "")

try:
    veces = int(input(color.GREEN + "¿Cuantas veces?" + color.RESET + ""))
except ValueError:
    print(" ")
    print(color.yellow + "ingrese un numero, no puede contener letras" + color.RESET + "")
    print(" ")
    sys.exit()

os.system("clear")

def email():
    try:
        message = (mensaje)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login((tucorreo), (contraseña))

        server.sendmail((tucorreo), (correo), message)

        server.quit()

        print(color.GREEN + 'Correo enviado ' + str(suma) + color.RESET + "")
    
    except smtplib.SMTPAuthenticationError:
        print(" ")
        print(color.yellow + "tu usuario o contraseña es incorrecto, prueba a cambiarlos" + color.RESET + "")
        print(" ")         
        sys.exit()
    
    except smtplib.SMTPRecipientsRefused:
        print(" ")
        print(color.yellow + correo + " no es un correo valido, prueba a cambiarlo" + color.RESET + "")
        print(" ")
        sys.exit()

for _ in range(veces):
    email()
    suma = suma + numero
