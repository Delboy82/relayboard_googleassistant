from gpiozero import OutputDevice
from time import sleep
 
relay1_pin = 14

relay1 = OutputDevice(relay1_pin, active_high=False, initial_value=False)
   
relay1.off()
 
