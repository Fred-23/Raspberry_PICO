##from machine import Pin
from machine import Pin, Timer
led = Pin(25,Pin.OUT)
tim=Timer()
def tick(timer):
    global led
    led.toggle()
    
    
tim.init(freq=1, mode= Timer.PERIODIC, callback=tick)
# led.value(1)
# led.value(0)