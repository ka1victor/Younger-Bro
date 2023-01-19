import pyautogui
import time
import random

def attack():
    fight_btn=pyautogui.locateOnScreen('fight.png')
    pyautogui.click(fight_btn)
    time.sleep(0.1+random.random()/10)
    pyautogui.click(fight_btn)

while True:
    attack()