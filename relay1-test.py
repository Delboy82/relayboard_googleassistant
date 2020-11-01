from RPi import GPIO
import time as t


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay1_pin = 14

GPIO.setup(relay1_pin, GPIO.OUT)

state = GPIO.input(relay1_pin)

if state:
   GPIO.output(relay1_pin,0)
else:
   GPIO.output(relay1_pin,1)




#relay1 = OutputDevice(relay1_pin, active_high=False, initial_value=None)

#relay1.toggle()
#time.sleep(5)

