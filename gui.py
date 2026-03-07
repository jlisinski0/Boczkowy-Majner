import customtkinter as ctk
import keyboard

def run(start_cb, stop_cb):
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()        
    app.geometry("500x500")
    app.title("BoczkowyMajner")
    app.iconbitmap("boczek.ico")
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

    def on_start():
        try:
            


            commands = [
                entryCommandOne.get(),
                entryCommandTwo.get(),
                entryCommandThree.get(),
                entryCommandFour.get()
            ]

            laps = [
                 entrySmallOne.get(),
                 entrySmallTwo.get(),
                 entrySmallThree.get(),
                 entrySmallFour.get(),
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


