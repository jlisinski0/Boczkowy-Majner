import pyautogui
import time


def command(commands, laps, lap_counter):
    pairs = [(cmd, lap) for cmd, lap in zip(commands, laps) if cmd.strip()]


  
    for cmd, lap in pairs:
        try:
            interval = int(lap)
        except ValueError:
            interval = 1.0
        if lap_counter % interval == 0:
            pyautogui.press('t')
            time.sleep(.2)
            pyautogui.write(cmd)
            time.sleep(.1)
            pyautogui.press('enter')
            time.sleep(.1)

