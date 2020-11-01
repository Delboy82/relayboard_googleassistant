from RPi import GPIO
import time as t


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay8_pin = 7

GPIO.setup(relay8_pin, GPIO.OUT)

state = GPIO.input(relay8_pin)

if state:
   GPIO.output(relay8_pin,0)
else:
   GPIO.output(relay8_pin,1)
