from RPi import GPIO
import time as t


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay7_pin = 8

GPIO.setup(relay7_pin, GPIO.OUT)

state = GPIO.input(relay7_pin)

if state:
   GPIO.output(relay7_pin,0)
else:
   GPIO.output(relay7_pin,1)
