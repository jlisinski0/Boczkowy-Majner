import pyautogui
import walk

def mine(blocks):
    pyautogui.mouseDown(button='left')
    walk.walking(blocks)
    pyautogui.mouseUp(button='left')