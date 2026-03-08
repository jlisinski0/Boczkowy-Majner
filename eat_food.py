import pyautogui
import time

def eat(eating, lap_counter):
    interval = int(eating)

    if lap_counter % interval == 0:
        pyautogui.press('2')
        pyautogui.mouseDown(button='right')
        time.sleep(3)
        pyautogui.mouseUp(button='right')
        pyautogui.press('1')