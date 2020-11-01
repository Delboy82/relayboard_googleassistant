from RPi import GPIO
import time as t


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay1_pin = 14

GPIO.setup(relay1_pin, GPIO.OUT)

state = GPIO.input(relay1_pin)

print (state)

if state:
   GPIO.output(relay1_pin,0)
else:
   GPIO.output(relay1_pin,1)
