import time
import RPi.GPIO as GPIO 
#from playsound import playsound
import keyboard
from getpass import getpass
from tkinter import *




####HUGE SIGN

print('''
 __          __  _                            _______     
 \ \        / / | |                          |__   __|  _ 
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___(_)
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \  
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) | 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___(_)
''')


print('''
RRRRRRRRRRRRRRRRR                  AAA               DDDDDDDDDDDDD           SSSSSSSSSSSSSSS 
R::::::::::::::::R                A:::A              D::::::::::::DDD      SS:::::::::::::::S
R::::::RRRRRR:::::R              A:::::A             D:::::::::::::::DD   S:::::SSSSSS::::::S
RR:::::R     R:::::R            A:::::::A            DDD:::::DDDDD:::::D  S:::::S     SSSSSSS
  R::::R     R:::::R           A:::::::::A             D:::::D    D:::::D S:::::S            
  R::::R     R:::::R          A:::::A:::::A            D:::::D     D:::::DS:::::S            
  R::::RRRRRR:::::R          A:::::A A:::::A           D:::::D     D:::::D S::::SSSS         
  R:::::::::::::RR          A:::::A   A:::::A          D:::::D     D:::::D  SS::::::SSSSS    
  R::::RRRRRR:::::R        A:::::A     A:::::A         D:::::D     D:::::D    SSS::::::::SS  
  R::::R     R:::::R      A:::::AAAAAAAAA:::::A        D:::::D     D:::::D       SSSSSS::::S 
  R::::R     R:::::R     A:::::::::::::::::::::A       D:::::D     D:::::D            S:::::S
  R::::R     R:::::R    A:::::AAAAAAAAAAAAA:::::A      D:::::D    D:::::D             S:::::S
RR:::::R     R:::::R   A:::::A             A:::::A   DDD:::::DDDDD:::::D  SSSSSSS     S:::::S
R::::::R     R:::::R  A:::::A               A:::::A  D:::::::::::::::DD   S::::::SSSSSS:::::S
R::::::R     R:::::R A:::::A                 A:::::A D::::::::::::DDD     S:::::::::::::::SS 
RRRRRRRR     RRRRRRRAAAAAAA                   AAAAAAADDDDDDDDDDDDD         SSSSSSSSSSSSSSS   
''')

print('\n')
print('The Remotely Activated Detonation System. \n')



print('Press ENTER to continue. Press any other key to exit')

#x = 0
#start (enter = start, any other key exits)
#while x == 0:
    #if keyboard.read_key() != "enter":
        #print("exiting...")
        #break
    #if keyboard.read_key() == "enter":
        #print('starting...')
        #print('\n')
        #x = x+1
x = 0
#once enter is pressed, sign in
while x == 0:
    password = getpass('Enter your password to authenticate detonation: ')
    
    if password != '1234':
        print('Verification failed.')
        time.sleep(1)
        exit()
        
    if password == '1234':
        print('Successfully verified!\n')
        time.sleep(2)
        print('ARMED: READY FOR DETONATION\n')
        time.sleep(1)
        exec(open("test.py").read())
        time.sleep(3)    
        x = x+1
        ##make program have 15 seconds to turn on (before test.py and so it turn off automaticly and theres some kind of gui countdown?
        


#
        
    #if keyboard.read_key() != 'enter':
        #print('CANCLED')
        #exit()
    #else:
     #   print('Authentication failed')
      #  exit()
        
