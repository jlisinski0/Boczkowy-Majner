
import pyautogui
import time


# One block = .215s

b = 0

def walk(x, key):
    x = x * .215 

    pyautogui.keyDown(key)
    time.sleep(x)
    pyautogui.keyUp(key)

    

def walking(blocks):
    walk(blocks, 'd')
    walk(1, 's')
    walk(blocks, 'a')
    walk(1, 'w')