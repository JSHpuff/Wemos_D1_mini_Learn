from machine import Pin, PWM
import time

beeper = PWM(Pin(2, Pin.OUT))

button1 = Pin(16, Pin.IN)
button2 = Pin(14, Pin.IN)
button3 = Pin(12, Pin.IN)
button4 = Pin(13, Pin.IN)
button5 = Pin(15, Pin.IN)
button6 = Pin(5, Pin.IN)
button7 = Pin(4, Pin.IN)

tones = {
    'c': 262,
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
}

while True:
    if button1.value() == 1:
        beeper.duty(512)
        beeper.freq(tones['c'])
    
    elif button2.value() == 1:
        beeper.duty(512)
        beeper.freq(tones['d'])
    
    elif button3.value() == 1:
        beeper.duty(512)
        beeper.freq(tones['e'])

    elif button4.value() == 1:
        beeper.duty(512)
        beeper.freq(tones['f'])

    elif button5.value() == 1:
        beeper.duty(512)
        beeper.freq(tones['g'])
    
    elif button6.value() == 1:
        beeper.duty(512)
        beeper.freq(tones['a'])

    elif button7.value() == 1:
        beeper.duty(512)
        beeper.freq(tones['b'])
    
    else:
        beeper.duty(0)

    time.sleep(0.05)