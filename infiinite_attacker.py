import pyautogui
import time
import random

def attack():
    fight_btn=pyautogui.locateOnScreen('fight.png') # check wheter it gets the center of the button of the top-and-left coordinates
    pyautogui.click(fight_btn)
    time.sleep(0.1+random.random()/10)
    pyautogui.click(fight_btn)

while True:
    attack()