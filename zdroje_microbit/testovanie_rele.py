from microbit import *

def senzor_narazu(pin):
    analogova_hodnota = pin.read_analog()
    if analogova_hodnota > 10:
        return False
    else:
        return True


while True:
    if senzor_narazu(pin1):
        pin2.write_digital(1)
        sleep(1000)
    else:
        pin2.write_digital(0)
        sleep(500)


