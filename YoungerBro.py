import pyautogui
import time
import random # only to make timing to seem more human like and avoid ban
import cv2
import pytesseract
import numpy as np

def identify_status(): #'walkaround' or 'battle'
    found = pyautogui.locateOnScreen('hp.png',region=(1055,610,30,20)) # @kaykyb's suggestion: load it once into a buffer, and then locate the buffer on the future times the function is called. That could make the function faster, and decrease the time spent between action
    if found == None: #check what is the actual error message
        return 'walkaround'
    else:
        return 'battle'

def go_right(length):
    global position
    pyautogui.keyDown('right')

    step_time=0.1 #just a guess
    while identify_status() == 'walkaround' and position < length:
        #time.sleep(step_time) #identify status takes around the time of two steps to run
        position = position + 2

    pyautogui.keyUp('right') #

def go_left():
    global position
    pyautogui.keyDown('left')

    step_time=0.1 #just a guess
    while identify_status() == 'walkaround' and position > 1:
        #time.sleep(step_time)
        position = position - 2

    pyautogui.keyUp('left') #

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

length = int(input("What is the line size?"))
position = int(input("What position are you in counting from left to right?\n"))
moves = int(input("How many moves (battles or walks) do you want the YoungerBro to make?"))

pyautogui.hotkey('alt','tab')
for i in range(moves): #quantas batalhas quer fazer    
    
    # WALK
    if identify_status() == 'walkaround':
        size=length/2
        if position < size:
            go_right(size) #size informs our function about its borders (in right)
        else:
            go_left() #size, here, is not needed, because the border is the position=1

    # BATTLE
    if identify_status() == 'battle':
        time.sleep(0.5+random.random())
        wild = identify_poke()
        pokemon = wild[0]
        is_shiny_or_elite = wild[1]

        # could be automated by doing a /pokemon, "reading" the species from that area, and classifying by rarity
        # we could also take this lists as user input before the loop
        kill_list = ['Weedle','Caterpie','Kakuna','Metapod','Butterfree']
        catch_list = []
        # meanwhile, since we're probably using large moves, and the bot is still only intended for people who can read this, this looks like a better approach

        if (pokemon in catch_list) or is_shiny_or_elite: # putting this first to be safe in case we put a poke into kill_list and catch_list
            call_me()
            #catching could be automated, but must be used wisely
        elif pokemon in kill_list:
            attack()
            time.sleep(9)
        else:
            print("Your poke is not on any list!")
            call_me()
        status = identify_status()
    
    # IMPROVEMENTS
    # implement call_me()
    # call_me() if someone sends you a trade/battle request
    # play and stop
    # pause and resume
    # create a run_list[]
    # use xposition and yposition to be able to walk in both dimensions