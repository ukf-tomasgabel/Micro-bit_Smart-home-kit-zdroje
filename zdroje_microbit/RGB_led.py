from microbit import *
from neopixel import NeoPixel

num_pixels = 12
np = NeoPixel(pin1, num_pixels)

def meranie_teploty(pin):
    analogova_hodnota = pin.read_analog()
    teplota = analogova_hodnota * (3300/1024)
    teplota = (teplota - 500)/10
    return teplota

while True:
    if meranie_teploty(pin2) >= 32:
        np[0] = (0, 255, 0)
        np.show()
        sleep(5000)
    else:
        np[0] = (255, 0, 0)
        np.show()
        sleep(500)
