import pygame
import time 
import csv
import collections 
import math

makeEvent = collections.namedtuple('Event', ['x','y','type', 'click_held'])
def getCSV(filename):
    with open(filename, 'r', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        
        eventList = [makeEvent(row[0],row[1],row[2], row[3]) for row in reader]
    return eventList
def main():
    pygame.init()
    white = (255,255,255)
    size = [600, 400]
    width, height = size
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Mouse Trail')

    
    running = True
    
    clock = pygame.time.Clock()
    screen.fill(white)
    pygame.display.flip()

    mouse_events = getCSV("eventlog.csv")
    
    for mouse_event in mouse_events:
        newevent = pygame.event.poll()
        if newevent.type == pygame.QUIT:
            pygame.quit()
            break
        clock.tick(50)
        
        if mouse_event.type == "click":
            
            pygame.draw.circle(screen, (255,0,0), (math.floor(int(mouse_event[0])/3.2), math.floor(int(mouse_event[1])/2.7)), 5)
            
        elif mouse_event.type == "move":
            pygame.draw.circle(screen,(0,0,255), (math.floor(int(mouse_event[0])/3.2), math.floor(int(mouse_event[1])/2.7)), 2)
        pygame.display.flip()
        
        
    
    while running:
        clock.tick(10) 
        event1 = pygame.event.poll()
        
        if event1.type == pygame.QUIT:
            running = False
            break
    pygame.quit()
        

        
        
    

if __name__ == "__main__":
    main()