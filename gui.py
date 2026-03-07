import customtkinter as ctk
import keyboard
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)


def run(start_cb, stop_cb):  

    ctk.set_appearance_mode("dark")



    app = ctk.CTk()        
    app.geometry("700x700")
    app.title("BoczkowyMajner 1.0")
    app.iconbitmap(resource_path("boczek.ico"))
    label = ctk.CTkLabel(app, text="BoczkowyMajner 2000")
    label.pack(pady=20)
    labelBlocks = ctk.CTkLabel(app, text="Na ile blokow stowniarka:")
    labelBlocks.pack(pady=5)
    entry = ctk.CTkEntry(app)
    entry.pack(pady=10)
    labelCommands = ctk.CTkLabel(app, text="Komendy które mam pisac: ")
    labelCommands.pack(pady=5)

    # Commands

    row1 = ctk.CTkFrame(app)
    row1.pack(pady=10)

    row2 = ctk.CTkFrame(app)
    row2.pack(pady=10)

    row3 = ctk.CTkFrame(app)
    row3.pack(pady=10)

    row4 = ctk.CTkFrame(app)
    row4.pack(pady=10)

    row5 = ctk.CTkFrame(app)
    row5.pack(pady=10)

    row6 = ctk.CTkFrame(app)
    row6.pack(pady=10)

    row7 = ctk.CTkFrame(app)
    row7.pack(pady=10)

    # First row 
    entryCommandOne = ctk.CTkEntry(row1, width=200)
    entryCommandOne.pack(side="left", padx=(0,5))

    entrySmallOne = ctk.CTkEntry(row1, width=30)
    entrySmallOne.pack(side="left")

    # Second row
    entryCommandTwo = ctk.CTkEntry(row2, width=200)
    entryCommandTwo.pack(side="left", padx=(0,5))

    entrySmallTwo = ctk.CTkEntry(row2, width=30)
    entrySmallTwo.pack(side="left")
    
    # Third row
    entryCommandThree = ctk.CTkEntry(row3, width=200)
    entryCommandThree.pack(side="left", padx=(0,5))

    entrySmallThree = ctk.CTkEntry(row3, width=30)
    entrySmallThree.pack(side="left")

    # Fourth row
    entryCommandFour = ctk.CTkEntry(row4, width=200)
    entryCommandFour.pack(side="left", padx=(0,5))

    entrySmallFour = ctk.CTkEntry(row4, width=30)
    entrySmallFour.pack(side="left")

    # Fifth row
    entryCommandFive = ctk.CTkEntry(row5, width=200)
    entryCommandFive.pack(side="left", padx=(0,5))

    entrySmallFive = ctk.CTkEntry(row5, width=30)
    entrySmallFive.pack(side="left")

    # Sixth row
    entryCommandSix = ctk.CTkEntry(row6, width=200)
    entryCommandSix.pack(side="left", padx=(0,5))

    entrySmallSix = ctk.CTkEntry(row6, width=30)
    entrySmallSix.pack(side="left")

    # Seventh row
    entryCommandSeven = ctk.CTkEntry(row7, width=200)
    entryCommandSeven.pack(side="left", padx=(0,5))

    entrySmallSeven = ctk.CTkEntry(row7, width=30)
    entrySmallSeven.pack(side="left")
    def on_start():
        try:
            


            commands = [
                entryCommandOne.get(),
                entryCommandTwo.get(),
                entryCommandThree.get(),
                entryCommandFour.get(),
                entryCommandFive.get(),
                entryCommandSix.get(),
                entryCommandSeven.get()
            ]

            laps = [
                 entrySmallOne.get(),
                 entrySmallTwo.get(),
                 entrySmallThree.get(),
                 entrySmallFour.get(),
                 entrySmallFive.get(),
                 entrySmallSix.get(),
                 entrySmallSeven.get(),
            ]

           
            blocks = int(entry.get())
            start_cb(blocks, commands, laps)
        except ValueError:
            print("Błąd")

    btn_start = ctk.CTkButton(app, text="Start (f8)", command=on_start)
    btn_start.pack(pady=5)

    btn_stop = ctk.CTkButton(app, text="Stop (f9)", command=stop_cb)
    btn_stop.pack(pady=5)

    keyboard.add_hotkey('f8', on_start)
    keyboard.add_hotkey('f9', stop_cb)
    
    app.mainloop()    


