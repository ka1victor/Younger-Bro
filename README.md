# Younger-Bro
TL;DR: A bot which levels up for you in Pokemon Planet by defeating common species and calling you when a rare one appear -- just like your YoungerBro.

# Why?
Pokemon Planet that kinf of MMORPG which requires a lot of time to level up. 
When I was tired of doing the same repetitive tasks, I would find a buddy (my brother, a close friend, a cousin...) and teach them:
"Kill these stupid worms, and call me if you find a Pikachu or another interesting Pokemon -- specially if you don't know them."

Sadly, we grew up. Eventually, they would not be that eager to level up. And I myself stopped playing it. 
Until I got started with Python scripting, I thought "What if..."
So, after a few years of procrastination, I just decided to built it with the support of the man himself, @kaykyb.



# How it works
1. YoungerBro gains control of mouse and keybaord, opens the game window and starts walking (PyAutoGUI)

2. Every once in a while, it looks at certain region of the screen to check if an HP bar appeared there, which means we are in battle (Open CV)

3. In the battle, it observes the pokemon name and whether it's shiny (PyTesseract) (and Numpy for buffer handling)

4. Finally, if the name is in the list of common ones (and it's not shiny), YoungerBro will attack. (PyAutoGUI)
But if it's shiny, or out of the kill list, YoungerBro will open an app like WhatsApp, Signal or Skype and literally call you. (PyAutoGUI, just to be quick)



# Notes
Tech used: Python 3 (PyAutoGUI, Time, OpenCV, PyTesseract, Numpy, Random)

Disclaimer: obviously, this is not allowed. So, use it wisely, or be prepare for athe possibility of getting banned.
Also, this is a mere prototype designed to run locally.
In order to use it, take a look at the files, install the necessary libraries (PyTesseract is annoying to install on Windows), adapt ates and run.
If you succed, you just saved a LOT of time leveling up in exchange for a few minutes.
-- to be honest, maybe a few hours if you're new to coding (but you'll learn a lot), or if you're using Windows (you'll learn changing OS might be a good idea).

Anyway... Congratulations, and good luck!! =)