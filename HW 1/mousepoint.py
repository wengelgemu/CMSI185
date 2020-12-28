'''
mousepoint.py
Name: Wengel Gemu
Collaborators: None 
Date: September 7th, 2019
Description: 
'''

from graphics import *

# create the graphics window
win = GraphWin("Mouse Pointer", 300, 300)

# TODO: add your code to draw the square!


#win.setBackground("blue")
point1 = Point(100,100)
point2 = Point(200,200)
aRectangle = Rectangle(point1, point2)
aRectangle.draw(win)
aRectangle.setFill("blue")

# get mouse coordinates
while True:
    # we will learn more about while loops in a couple weeks
    # for now all your code must be within this loop,
    #   without the loop you would only be able to click once!
    p = win.getMouse()
    x = p.getX()
    y = p.getY()
    print('x: ', x, ', y: ', y)

    # TODO: add your code here!
#   check if the point is inside
    if (100 <= x <= 200) and (100 <= y <= 200):
        aRectangle.setFill("green")
        print("green")
    else:
        aRectangle.setFill("red")
        print("red")


# process events (don't change/move this)
win.mainloop()
