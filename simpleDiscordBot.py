#Trzeba zbudować bota w Pythonie...
#jakiś pomysł?

import pyautogui
import time

time.sleep(10)

f = open("text.txt","r")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")



