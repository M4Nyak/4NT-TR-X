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

                                                                                
                                       ^7?YYJ?~:                                                    
                                     ~5P5YY5J5#G5?.                                                 
                                    !BYJPGG5JPBPG#G!                                                
                                    ?BYY5YYPPPPPB55B?                                               
                                    ^#GPP5Y5YYPP5YYYBJ                                              
                                     7BG55J?JYJ?JY5Y5BJ                                             
                                      :YGPJ7~~7JJJ5YYP#Y                                            
                                        :JGPJ!^!JJJ5GPYBJ                                           
                                          :7PPY77Y555YYYBY...                            :~~~^..    
                                            .!PGJ!7JJ5YY5#GPPPPP5YY?~:.                !555YYYYY?^ .
                                            .:!BBJ?JJ5555#GPPPPPPGGGGGP57    :       ~PP#5?5GPP5YP! 
                                           ?PGPG#55YYPPPG#GGBGGGGGPPPPB&Y  .5BPJ~.  :BBYJPP5YYYYJP5 
                                          7#555BBPPPPGGGBBBBBBGGGGGBB#B#~ ^GBPPGBP?:YGJ5JYY5GGGGGB5.
                                         ^BBPPP55555555555555PGBBBBGGGGBPJBGPPPPPPBBBJ7^?555GGGGGBG.
                                      :75P55555YYYYYYYYYYYY5555YY5GBBBGGGBBBBPPPPPP#5?^!JJJ55555PG^ 
                                    ^YP5555YYY55555555PPP555YYY5P5JYPBBBBGPGBBBPPPB#Y^~JJJYYYYYG5:  
                                  :YG55PYJ5P55555PGGGBGBGGGPPPPYJYPPJJPBGBBGPGB#GG#YY?JJJYYYY5GJ.   
                                 !G5YPYJ5PYY5GBBBBBBBBBB#####BGGG5JYG5?YGGGBGGGB#B57~J55PPPPGP!     
                                7BY5P?YGYJ5PYY5PGGGGGGGBBBBBBB##BGGYJPP?JPBPBB5PGY??JJYY5Y5GB:      
                               !#JYG?5GJYGY?J?JJJY5PGGGGGGGBBBBB##BBY?PP??GBGB5?JG5YYYYYY5BBBJ      
                             .J#5?GJJBJYGJ?JJJJJJJJJJYPGGGGGGGBBBBB#BJJGY?JBGG#5YYBY555PG#BGG#J     
                            !G#B?YG!PPJBJ?JJJJJJJJJJJJ?JJYPGGGGGGBBB#5?5P??PBPBBPGBBBBB##GGGBG#!    
                          .Y#PBG?5P~GY5G?JJJJJJJJJJJJJJJJJJJJ5PGGGGG#P?YG??5#PG#GGGBBBBB##GGGGBG.   
   .~7?JJ???!^           ~G#GB#G?YG^P55P?JJJJJJJ??J??JJJJJJJJJ?JY5PG#5?5P??5#PG#GGGGBGBBB##GGGG#~   
  !PPYYYGBY5#P5J!:.     :B#BBG#B??B77GYGJJJJYYY5555P5?JJJJJJJJJJJJ?JBJ?GY??PBPG#GGGGBBBBBB##GGB#~   
 7BY?BP?5BJ75J7J5P5J!:  :##BGPG&Y7YG75PPBGGGGGGGPPP5B5JJJJJJJJJJJJ?G575P??JBGGB#GGGBBBBBBBB#BB5!.   
.GP?YBJJB5JJPY~~^~7J5PP?5&#GPGG##J75P?YGGBGGGGGGGGGPPB5?JJJJJJJJ?YG575GJ??GBPG#BGGBBBBBBBBB#&J      
 7B5Y5PB5JJ5GJJJ?7!~~~PY5PPB5J?Y#B?7JPJJ5GBBBBBBGGGGGPB5JJJJJJJYPGJ?P5???PBPGB#BBBBBBBBBBBBB&?      
  ~G#GP55PPPJJJJJJJJJJG7?JJG???7Y#BY775PYJ5G##BBBBBGGGGBY?JJJ5PPJJ5PY??JGBPGB#BB#BBBBBBBBBBB&Y      
   .?5GBGP5YYYYYYJJJYGYJJJJ5PJJJ?5#BP?77Y55YY5PGBBBBBBBBB5555YJY55J??J5BGPGBBG#BBBBBBBBBBBB#B:      
      .^!JYPPPPP55PPPYYYYYYY5PGPPGGGBBPJ77?Y555YYY555YYYYYYY555Y???Y5BGPGBBBGBB##B#BBBBBB#&P:       
           .:^!??P#GPPP5555PPGBGP55Y5GBBGPY????JYYY55555YYYJJ??JY5GBGPGBBBGGBBBB#B#BBB###G7         
                ~GBPGGGBBBBGGGPPPPP555B#GBBBGP5YJJJJJJ?JJJJY55PGGGGGBBBBGBBB##BB##&###GJ~.          
              ^5BGPGGBBBBBBBBBBBBBBBGBBPGBPJPBBBGGGGGGGGGGGGGGGGGBBBBGGB#BBB##BB#G7J7^.             
            .?BBBBBBBGGGGGGGGBBBBBGGBBBBY~:7GGPGGGBGBGGGGGGGB#GB#BGGGGB##B###BBB#P                  
           ~G&BBBGGGGBBBBBB#G5YY55PPGGJ^  7&BGGP555P#P555555P#GPGB#BBBBB##BBBBB##?                  
          ?##BGGGGBBBBBGGBBY:      ...    ~&GGGBBGPP#5J7JYJYYBBGGGG##BBBBBBBBB#B!                   
         7#BGGGGB#BGGGBBGY^               .YGBBGGBBB#GY7J5Y55B#GGGGG##BBBBBBB#5:                    
         G#GGGGB#BBBBGY!.                   .~YBBGG#BYY?5P5PP5#GGGGGB#BBBBB##?                      
        .GBGGGB##G5?~.                         :JBB#BPPJ555GGG##GGBBB#BBBB#G^                       
         J##BGY7^.                               ~#GYP5YYYY5PPP#BPGGB#BB##J.                        
          ~!:.                                   !#YGY??JJYJJPPP#PPB####B!                          
                                                 ^#5GJJPGGGY?5GP#GG&BGPJ:                           
                                                  7GGPYJJJ?J5GG#GG&?:.                              
                                                   :?PBBGPGBBBBGP#5                                 
                                                     ~#BGG#BPGPP#P.                                 
                                                    !B#GPPB#GGG#G:                                  
                                                   ?#B#BGGB#GG#G:                                   
                                                 .Y#GB#GGGBBG#5.                                    
                                                :P#GB#BGGG###?                                      
                                               !B#BBBGGGG##P^                                       
                                             .J#BBBGGGGB#G!                                         
                                            :5#GGGGBB#B5!.                                          
                                           ~G#BBBGP5J!:                                             
                                           ~~~~^:.   
                   
                    
                     
                      
                       
                        
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
