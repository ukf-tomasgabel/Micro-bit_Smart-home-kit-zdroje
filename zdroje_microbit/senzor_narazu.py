from microbit import *

def senzor_narazu(pin):
    x = pin.read_analog()
    if x > 10:
        return False
    else:
        return True


while True:
    if senzor_narazu(pin2):
        print("zopnutý")
    else:
        print("nezopnutý")
    sleep(200)


