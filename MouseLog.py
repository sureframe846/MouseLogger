from pynput import mouse
import time
import collections 
import csv

makeEvent = collections.namedtuple('Event', ['x','y','type', 'click_held'])
allEvents = []
stateOn = False
click_held = False

def on_move(x, y):
    # print('Pointer moved to {0}'.format(
    #     (x, y)))
    event1 = makeEvent(x,y,"move", click_held)
    print('Pointer moved to {0}: click is held'.format((event1.x, event1.y))) if click_held \
    else print('Pointer moved to {0}'.format((event1.x, event1.y)))
    
    allEvents.append(event1)

def on_click(x,y, button, pressed):
    global click_held
    if pressed:
        click_held = True
        event1 = makeEvent(x,y,"click", click_held)
        print("Click at {0}".format((event1.x,event1.y)))
    else: 
        click_held = False
        event1 = makeEvent(x,y,"release", click_held)
       
        print("{0} Released".format((x,y)))
    allEvents.append(event1)
def startLog():
    global stateOn
    stateOn = True
    print("Starting Log")
    listener.start()
    
def stopLog():
    global stateOn
    if stateOn:
        stateOn = False
        listener.stop()
        
        
        print(listener.is_alive())
        
        outputCSV()
    else:
        print("Cannot stop log: Log is not on")

def outputCSV():
    with open("eventlog.csv", 'w', newline = '') as file:
        writer = csv.writer(file)
        for event in allEvents:
            writer.writerow(event)

listener = mouse.Listener(
    on_move=on_move,
    on_click = on_click)


    
