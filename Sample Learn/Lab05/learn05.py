from machine import ADC
import time

A0 = ADC(0)

while True:
    print(A0.read())
    time.sleep(0.05)