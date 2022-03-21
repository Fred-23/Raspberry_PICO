#Faire un multimètre d'abord
#Puis faire un oscilloscope avec des boutons sur tkinter pour l'échelle de temps, etc..
#ça peut être nice et pas si compliqué
#import machine # Pb récurrent ne marche pas pour beaucoup de gens car la librairie est mal installée
#obliger de nommer tous le temps je me rappelle des cours de liebeaux voir mon CR
#from machine import Pin
#from machine import ADC
from machine import *

G_tension = Pin(0,Pin.OUT,Pin.PULL_DOWN)
led = Pin(25,Pin.OUT)
G_tension.value(0)
led.value(0)
#ADC0 = Pin(26,Pin.ANALOG) 
# générer une tension avec ou des signaux avec les output
#pas de DAC à priori donc compliqué pour générer une rampe
adc = ADC(26)
while True :
    val  = adc.read_u16()
    tension = (val*3.3)/65535
    print("ADC0 :",tension)
    if(tension>=3.3) :
        led.value(1)
