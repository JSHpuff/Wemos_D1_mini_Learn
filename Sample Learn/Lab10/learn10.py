from machine import Pin, PWM
import time

beeper = PWM(Pin(2, Pin.OUT))

notes = [
    392, 330, 330, 0,
    349, 294, 294, 0,
    262, 294, 330, 349, 392, 392, 392, 0
]

for note in notes:
    if note == 0:
        beeper.duty(0)

    else:
        beeper.duty(512)
        beeper.freq(note)

    time.sleep(0.2)
    beeper.duty(0)
    time.sleep(0.1)