import pyautogui
import time
import random
import cv2
import pytesseract
import numpy as np

from PIL import Image

hp_img_file = open('hp.png', 'rb')
hp_img = Image.open(hp_img_file)

def identify_status(): #'walkaround' or 'battle'
    global hp_img
    found = pyautogui.locateOnScreen(hp_img, confidence=0.8) # @kaykyb's suggestion: load it once into a buffer, and then locate the buffer on the future times the function is called. That could make the function faster, and decrease the time spent between action
    if found == None: #check what is the actual error message
        return 'walkaround'
    else:
        return 'battle'

def go_right(length):
    global position
    pyautogui.keyDown('down')

    #step_time=0.01
    while identify_status() == 'walkaround' and position < length: #this loop's processing time (IN THIS VERSION) means a lot of step_time
        position = position + 7

    pyautogui.keyUp('down') #

def go_left():
    global position
    pyautogui.keyDown('up')

    #step_time=0.01
    while identify_status() == 'walkaround' and position > 1: #this loop's processing time (IN THIS VERSION) means a lot of step_time
        position = position - 7

    pyautogui.keyUp('up') #

def identify_poke():
    """info_bar must be a tuple the information (left, top, width, heith) of your the opposing poke showing up above your HP bar, from its name to its level."""
    
    sc = pyautogui.screenshot(region=(1038, 361, 216, 18)) #what is the right region?
    image = cv2.cvtColor(np.array(sc),cv2.COLOR_RGB2BGR)
    text = pytesseract.image_to_string(image)

    all_words = text.split()
    name = all_words[0]
    if len(all_words)>1:
        shiny_or_elite = (all_words[1],all_words[2])
    else:
        shiny_or_elite = False
    return [name,shiny_or_elite]

def attack():
    fight_btn=pyautogui.locateOnScreen('fight.png',grayscale=0.5)
    pyautogui.click(fight_btn)
    time.sleep(0.1+random.random()/10)
    pyautogui.click(fight_btn)
    # Improvement: we could customize t he attack for each pokemon on that area. For instance, get the attack slot by looking the pokemon at: {'ratata' : 3, 'pidgey' : 2}, and direct the second click to the slot position

def call_me():
    #Open Whatsapp and call me with Pyautogui
    return 0

size = 9 #what is the line size?
position = int(input("What position are you in?\n")) #where in the line did you start, counting from 1 to size?
pyautogui.hotkey('alt','tab')

for i in range(10): #quantas batalhas quer fazer    
    status = identify_status()
    # WALK
    if status == 'walkaround':
        if position < size/2:
            go_right(size) #size informs our function about its borders (in right)
        else:
            go_left() #size, here, is not needed, because the border is the position=1

    # BATTLE
    if status == 'battle':
        wild = identify_poke()
        pokemon = wild[0]
        is_shiny_or_elite = wild[1]

        kill_list = ['Weedle','Caterpie','Kakuna','Metapod'] #could be automated by doing a /help, reading, and classifying each of the possible pokes by appearing
        catch_list = [] 

        if (pokemon in catch_list) or is_shiny_or_elite:
            call_me()
            #catching could be automated, but must be used wisely
        elif pokemon in kill_list:
            attack()
            time.sleep(8)
        else:
            print("Your poke is not on any list!")
            call_me()
        status = identify_status()
    
    # IMPROVEMENTS
    # call_me() if someone sends you a trade/battle request
    # play and stop
    # pause and resume
    # create a run_list[]
    # use xposition and yposition to be able to walk in both dimensions