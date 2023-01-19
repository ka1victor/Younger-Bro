import pyautogui
import time
import random
import cv2
import pytesseract
import numpy as np

#pyautogui.hotkey('alt','tab')
#time.sleep(2)

attack()
print('done')

# length = 21 #what is the line size?
# position = 8 #where in the line did you start?
# status = functions.identify_status()

# for i in range(3): #quantas batalhas quer fazer    
#     # WALK
#     if status == 'walkaround':
#         if position < length/2:
#             functions.go_right(21)
#         else:
#             functions.go_left(21)