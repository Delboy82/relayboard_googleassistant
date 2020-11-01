from RPi import GPIO
import time as t


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay6_pin = 25

GPIO.setup(relay6_pin, GPIO.OUT)

state = GPIO.input(relay6_pin)

if state:
   GPIO.output(relay6_pin,0)
else:
   GPIO.output(relay6_pin,1)
