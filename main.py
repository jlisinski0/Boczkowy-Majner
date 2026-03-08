import threading
import time
from mining import mine
import gui
import type_command
import eat_food

running = False
lap_counter = 0

def start(blocks, commands, laps, eating):
    global running
    global lap_counter

    if running:
        return
    
    running = True

    def loop():
        global lap_counter
        time.sleep(2)

        while running:
            mine(blocks)
            lap_counter += 1
            type_command.command(commands, laps, lap_counter)
            eat_food.eat(eating, lap_counter)
            
       

    threading.Thread(target=loop, daemon=True).start()

def stop():
    global running
    running = False


if __name__ == "__main__":
    gui.run(start, stop)