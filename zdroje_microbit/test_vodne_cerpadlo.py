from microbit import *

rele = pin2

def meranie_vlhkosti(pin):
    analogova_hodnota = pin.read_analog()
    if analogova_hodnota <= 50:
        return True
    else:
        return False


while True:
    if meranie_vlhkosti(pin1):
        rele.write_digital(1)
        sleep(1000)
    else:
        rele.write_digital(0)
        sleep(1000)


