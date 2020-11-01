from RPi import GPIO
import time as t


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay2_pin = 15

GPIO.setup(relay2_pin, GPIO.OUT)

state = GPIO.input(relay2_pin)

if state:
   GPIO.output(relay2_pin,0)
else:
   GPIO.output(relay2_pin,1)
