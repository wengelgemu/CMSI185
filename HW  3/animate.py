'''
animate.py
Name: Wengel Gemu
Collaborators: Shane 
Date: September 20, 2019
Description: This shows a ball bouncing back and forth across the screen.
'''

from graphics import *
from time import sleep   # for pausing between frames

win = GraphWin("Ball", 300, 300)

# a circle is drawn at position (100, 150) on the board
c = Circle(Point(50, 100), 25)
c.setFill('blue')
c.draw(win)
centerPoint = c.getCenter

# make the whoel function look
for i in range (1, 6, 1):
    for i in range (1, 5, 1):
        
        centerPoint = c.getCenter

        # get ball to pause for .2 sec
        time.sleep(.2)
        # move the ball
        c.move(50, 0)
        # bouce ball
        time.sleep(.2)
        c.move(0, 100)
        time.sleep(.2)
        c.move(0, -100)
        # made sure that the ball goes edge to edge and not off the screen
        if centerPoint == 300 or centerPoint == 0:
            i += 1
            print('edge count: ' + str(i))
        if i == 10:
            break

    for i in range (1, 5, 1):
        
        centerPoint = c.getCenter

        # get ball to pause for .2 sec
        time.sleep(.2)
        # move the ball
        c.move(-50, 0)
        # bouce ball
        time.sleep(.2)
        c.move(0, 100)
        time.sleep(.2)
        c.move(0, -100)
        # made sure that the ball goes edge to edge and not off the screen
        if centerPoint == 300 or centerPoint == 0:
            edge += 1
            print('edge count: ' + str(i))
        if i == 10:
            break


## TODO: define variables for the ball's location and velocity


# TODO: animate the ball, limiting it to 10 bounces
# hint: look at the code we wrote the first week in ufo.py


win.mainloop()
