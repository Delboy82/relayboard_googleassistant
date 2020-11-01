from RPi import GPIO
import time as t


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay3_pin = 18

GPIO.setup(relay3_pin, GPIO.OUT)

state = GPIO.input(relay3_pin)

if state:
   GPIO.output(relay3_pin,0)
else:
   GPIO.output(relay3_pin,1)
