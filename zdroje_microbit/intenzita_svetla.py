from microbit import *

def intenzita_svetla(pin):
    analogova_hodnota = pin.read_analog()
    return analogova_hodnota


while True:
    x = intenzita_svetla(pin1)
    print(x)
    sleep(500)

