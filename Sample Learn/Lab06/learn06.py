from machine import ADC, Pin

A0 = ADC(0)
LED = Pin(15, Pin.OUT)

while True:
    if A0.read() < 100:
        LED.value(1)
    else:
        LED.value(0)