import RPi.GPIO as GPIO
import time

channel=21

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)

if __name__ == '__main__':
    try:
        motor_on(channel)
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass