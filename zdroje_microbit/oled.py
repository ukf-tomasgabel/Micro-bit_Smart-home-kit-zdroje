from microbit import *
from ssd1306 import *
from ssd1306_text import *

def meranie_teploty(pin):
    analogova_hodnota = pin.read_analog()
    teplota = analogova_hodnota * (3300/1024)
    teplota = (teplota - 500)/10
    return teplota

initialize()

while True:
    teplota1 = meranie_teploty(pin2)
    teplota_text = str(teplota1)
    clear_oled()
    add.text(0, 0, "Teplota: ")
    add_text(3, 1, teplota_text)
    sleep(1000)
