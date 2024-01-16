import keyboard
import mouse
import time

isClick = False

def set_clicker():
    global isClick
    if isClick:
        isClick = False
        print("Nestrādā")
    else:
        isClick = True
        print("Strādā")

keyboard.add_hotkey('Alt + Z', set_clicker)

while True:
    if isClick:
        mouse.double_click(button='left')
        time.sleep(0.01)
