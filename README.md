# MouseLogger
 
Records mouse data to a CSV.
Data recorded includes the event's position, type (click or movement), whether the click is held (used to show movements that occur while clicking), timer (the lifespan of an event), and movement group.   

Pauses in user input trigger new movement groups. The goal is to understand individual events in a larger context- moving the mouse across the screen creates many successive events, which should all be grouped together. 
