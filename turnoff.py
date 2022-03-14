'''NOTE
this script is super sketchy: the script tells the relay to turn on, and then off
when the button is pressed, but the relay is already on due to the previous script.
'''
import RPi.GPIO as GPIO
import time
import tkinter as tk

#boring setup (GPIO)
channel = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    
def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)

#end of setup

def write_text():
    print("DETONATION STATUS: -")
    exec(open("relayoff.py").read())
    GPIO.cleanup()
    

    


parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

##self expanitory
exit_button = tk.Button(frame,
                   text="CUT CIRCUIT",
                   fg="purple",
                   command=write_text)
                   


exit_button.pack(side=tk.RIGHT)

parent.mainloop()













