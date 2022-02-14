import smtplib
import os
import sys
import time
suma = 1

def banner():
    print(bcolors.GREEN + """
 _____ __  __    _    ___ _           ____ _   _  ___  ____ _____
| ____|  \/  |  / \  |_ _| |         / ___| | | |/ _ \/ ___|_   _|
|  _| | |\/| | / _ \  | || |   _____| |  _| |_| | | | \___ \ | |  
| |___| |  | |/ ___ \ | || |__|_____| |_| |  _  | |_| |___) || |  
|_____|_|  |_/_/   \_\___|_____|     \____|_| |_|\___/|____/ |_|  
                                                                   """ + bcolors.RESET)

class bcolors:
    GREEN = "\033[92m"
    RESET = "\033[0m"
    yellow = "\033[93m"
    cyan = "\033[36m"

banner()

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
message = input(bcolors.GREEN + "¿que mensaje quieres spamear?" + bcolors.RESET + "")

try:
    veces = int(input(bcolors.GREEN + "¿Cuantas veces?" + bcolors.RESET + ""))
except ValueError:
    print(" ")
    print(bcolors.yellow + "ERROR" + bcolors.RESET + "")
    print(" ")
    sys.exit()

e = time.time()
os.system("clear")

def email():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login((tucorreo), (contraseña))

        server.sendmail((tucorreo), (correo), message)

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

banner()
print("")

for _ in range(veces):
    email()
    suma = suma + 1

    if(veces == suma - 1):
        t = time.time()
        ti = t - e
        se = round(ti)
        dias = se // (24 * 60 * 60)
        se = se % (24 * 60 * 60)
        horas = se // (60 * 60)
        se = se % (60 * 60)
        minutos = se // 60
        se = se % 60
        print("")
        print(bcolors.yellow + "spam terminado correctamente")
        print("correos enviados:", veces)
        print('tiempo: dias: {} - horas: {} - minutos: {} - segundos: {}'.format(dias, horas, minutos, se) + bcolors.RESET + "")
