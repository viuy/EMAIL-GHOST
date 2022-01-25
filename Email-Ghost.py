import smtplib
import os
import sys
suma = 0
numero = 1

class bcolors:
    GREEN = "\033[92m"
    RESET = "\033[0m"
    yellow = "\033[93m"
    cyan = "\033[36m"

print(" ")
print(bcolors.yellow + "EMAIL-GHOST")
print(" ")
print(bcolors.yellow + "by VIUY" )
print(bcolors.cyan + "TikTok: viuy.tt" )
print("instagram: viuy_ig")
print(" ")
print(bcolors.GREEN + "bienvenido,para usar este script entra a:")
print("https://myaccount.google.com/lesssecureapps y permite el acceso de aplicacioes poco seguras")
print("(con la cuenta con la que vayas a spamear).")
print(" ")

tucorreo = input("¿con que correo quieres spamear?" + bcolors.RESET + "")
contraseña = input(bcolors.GREEN + "¿cual es la contraseña del correo?" + bcolors.RESET + "")
correo = input(bcolors.GREEN + "¿a que correo quieres espamear?" + bcolors.RESET + "")
mensaje = input(bcolors.GREEN + "¿que mensaje quieres spamear?" + bcolors.RESET + "")

try:
    veces = int(input(bcolors.GREEN + "¿Cuantas veces?" + bcolors.RESET + ""))
except ValueError:
    print(" ")
    print(bcolors.yellow + "ERROR" + bcolors.RESET + "")
    print(" ")
    sys.exit()

	@@ -48,20 +49,24 @@ def email():

        server.quit()

        print(bcolors.GREEN + 'Correo enviado ' + str(suma) + bcolors.RESET + "")

    except smtplib.SMTPAuthenticationError:
        print(" ")
        print(bcolors.yellow + "tu usuario o contraseña es incorrecto, prueba a cambiarlos" + bcolors.RESET + "")
        print(" ")         
        sys.exit()

    except smtplib.SMTPRecipientsRefused:
        print(" ")
        print(bcolors.yellow + correo + " no es un correo valido, prueba a cambiarlo" + bcolors.RESET + "")
        print(" ")
        sys.exit()

if(veces == suma):
    print(" ")
    print(bcolors.yellow + "spam terminado correctamente")

for _ in range(veces):
    email()
    suma = suma + numero
