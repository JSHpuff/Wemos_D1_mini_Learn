from machine import Pin
import time

# 建立串列, 依序儲存 D0、D5、D6、D7、D8、D1、D2 腳位編號
leds = [16, 14, 12, 13, 15, 5, 4]

while True:
    for i in leds:
        led = Pin(i, Pin.OUT)
        led.value(1)
        time.sleep(0.1)
        led.value(0)