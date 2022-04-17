from microbit import *

ventilator = pin2

def meranie_teploty(pin):
    analogova_hodnota = pin.read_analog()
    teplota = analogova_hodnota * (3300/1024)
    teplota = (teplota - 500)/10
    return teplota


while True:
    if meranie_teploty(pin1) > 32.5:
        ventilator.write_digital(1)
        sleep(8000)
        ventilator.write_digital(0)
        sleep(2000)
    else:
        ventilator.write_digital(0)
        sleep(300)
