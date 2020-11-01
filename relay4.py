from RPi import GPIO
import time as t


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay4_pin = 23

GPIO.setup(relay4_pin, GPIO.OUT)

state = GPIO.input(relay4_pin)

if state:
   GPIO.output(relay4_pin,0)
else:
   GPIO.output(relay4_pin,1)
