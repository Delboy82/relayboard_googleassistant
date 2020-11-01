from RPi import GPIO
import time as t


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay5_pin = 24

GPIO.setup(relay5_pin, GPIO.OUT)

state = GPIO.input(relay5_pin)

if state:
   GPIO.output(relay5_pin,0)
else:
   GPIO.output(relay5_pin,1)
