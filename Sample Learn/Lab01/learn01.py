from machine import Pin
import time

led = Pin(15, Pin.OUT)

led.value(1)
time.sleep(3)
led.value(0)