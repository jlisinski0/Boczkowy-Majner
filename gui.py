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
    app.title("BoczkowyMajner 1.1")
    app.iconbitmap(resource_path("boczek.ico"))
    label = ctk.CTkLabel(app, text="BoczkowyMajner 2000")
    label.pack(pady=20)
    labelBlocks = ctk.CTkLabel(app, text="Na ile blokow stowniarka:")
    labelBlocks.pack(pady=5)
    entry = ctk.CTkEntry(app)
    entry.pack(pady=10)

    labelFood = ctk.CTkLabel(app, text="Co ile jeść: ")
    labelFood.pack(pady=5)
    entryFood = ctk.CTkEntry(app)
    entryFood.pack(pady=10) 

    labelCommands = ctk.CTkLabel(app, text="Komendy które mam pisac: ")
    labelCommands.pack(pady=5)

    def createRow():
        name = ctk.CTkFrame(app)
        name.pack(pady=10)
        return name

    rows = [createRow() for i in range(7)]

    def displayRow(row):
        entry = ctk.CTkEntry(row, width=200)
        entry.pack(side="left", padx=(0,5))
        return entry

    def packRow(row):
        entry = ctk.CTkEntry(row, width=30)
        entry.pack(side="left")
        return entry

    entryCommand = []
    entrySmall = []

    for i in range(7):
        entryCommand.append(displayRow(rows[i]))
        entrySmall.append(packRow(rows[i]))

    def on_start():
        try:
            commands = [entryCommand[i].get() for i in range(7)]

            laps = [entrySmall[i].get() for i in range(7)]
           
            blocks = int(entry.get())
            eating = int(entryFood.get())
            start_cb(blocks, commands, laps, eating)

        except ValueError:
            print("Błąd")

    def stop_cb():
        app.quit()

    btn_start = ctk.CTkButton(app, text="Start (f8)", command=on_start)
    btn_start.pack(pady=5)

    btn_stop = ctk.CTkButton(app, text="Stop (f9)", command=stop_cb)
    btn_stop.pack(pady=5)

    keyboard.add_hotkey('f8', on_start)
    keyboard.add_hotkey('f9', stop_cb)
    
    app.mainloop()    


