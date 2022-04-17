from microbit import *

servo = pin1
#Konfigurovanie Micro:bita na vysielanie 50 Hz impulzov
servo.set_analog_period(20)

def senzor_narazu(pin):
    analogova_hodnota = pin.read_analog()
    if analogova_hodnota > 10:
        return False
    else:
        return True

while True:
    if senzor_narazu(pin2):
        pin1.write_analog(1023 * 1.0 / 20)
        sleep(2000)
        pin1.write_analog(1023 * 2.0 / 20)
        sleep(2000)
    else:
        print("Nič sa nedeje")
