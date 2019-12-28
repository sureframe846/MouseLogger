import tkinter as tk
from pynput import mouse
import MouseLog 
import drawer

root = tk.Tk() 

def update_btn_txt(text = ""):
    btn_text.set(text)
def startLogger():
    update_btn_txt("Stop Log")
    active.set(True)
    MouseLog.startLog()
def stopLogger():
    MouseLog.stopLog()
    update_btn_txt("New Log")
    active.set(False)
def buttonCommand():
    print(active.get())
    if active.get():
        print("Stopping Log")
        stopLogger()
        #button.pack_forget()
        draw_button.pack()
        quit_button.pack()
    else:
        print("Starting Log")
        startLogger()
def makeDrawing():
    drawer.main()

active = tk.BooleanVar()
active.set(False)
btn_text = tk.StringVar()
btn_text.set("Start Log")
root.title('Mouse Tracker') 

button = tk.Button(root, textvariable=btn_text, width=25, command=buttonCommand)

draw_button = tk.Button(root, text = "Draw it!", width =25, command = makeDrawing)
quit_button = tk.Button(root, text = "Quit", width = 25, command = root.destroy)
btn_text.set("New Log")

button.pack() 
root.mainloop()


