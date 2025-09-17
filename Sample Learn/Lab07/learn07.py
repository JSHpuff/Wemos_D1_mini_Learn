from machine import Pin, PWM
import time

LED = PWM(Pin(15))

while True:
    for i in range(200, 1024, 10):
        LED.duty(i)
        time.sleep(0.01)
    
    for i in range(1023, 199, -10):
        LED.duty(i)
        time.sleep(0.01)
