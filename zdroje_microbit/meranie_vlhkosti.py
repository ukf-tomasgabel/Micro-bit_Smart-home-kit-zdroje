from microbit import *

def meranie_vlhkosti(pin):
    analogova_hodnota = pin.read_analog()
    if analogova_hodnota <= 50:
        return "Pôda je suchá"
    elif analogova_hodnota > 50 and analogova_hodnota <= 500:
        return "Pôda je trochu vlhká"
    elif analogova_hodnota > 500:
        return "Pôda je vlhká"


while True:
    x = meranie_vlhkosti(pin1)
    print(x)
    sleep(200)


