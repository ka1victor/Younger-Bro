import pyautogui
import time


def mouse_position(wait):
    time.sleep(wait)
    x, y = pyautogui.position()
    return "x: "+str(x)+" ; y: "+str(y)

pyautogui.hotkey('alt','tab')

print(mouse_position(5))

#(675,650,125,40)
