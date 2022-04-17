from microbit import *

def meranie_teploty(pin):
    analogova_hodnota = pin.read_analog()
    teplota = analogova_hodnota * (3300/1024)
    teplota = (teplota - 500)/10
    return teplota


while True:
    print(meranie_teploty(pin1))
    sleep(200)

