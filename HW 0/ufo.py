'''
ufo.py
Name: Wengel Gemu
Collaborators: None
Date: August 28th, 2019
Description: Draw a scene with a UFO using graphics.
'''

from graphics import *
from time import sleep  # for pausing between frames


##### Functions ######

# draw the blue sky, grass, and yellow sun
def draw_scenery():
    grass_height = 100
    sun_radius = 100

    # draw blue sky
    win.setBackground("cyan")

    # TODO: draw the grass as a green rectangle

    point1 = Point(0,300)
    point2 = Point(300,300-grass_height)
    grass = Rectangle(point1, point2)
    grass.draw(win)
    grass.setFill("green")


    # TODO: draw the sun as a yellow circle
    point = Point(220,50)
    sun = Circle((point), 30)
    sun.draw(win)
    sun.setFill("yellow")


def draw_oval(width, height, x, y):
    point1 = Point(x,y)
    point2 = Point(x + width, y + height)
    ufo = Oval(point1, point2)
    ufo.draw(win)
    ufo.setFill("grey")

    return ufo

# TODO: draw the UFO as two gray ovals (specified by points on bounding box)
def draw_ufo():
    # bottom oval
    wide_oval = draw_oval(100, 50, 65, 113)

    # top oval
    narrow_oval = draw_oval(50, 40, 90, 100)

    return (narrow_oval, wide_oval)

# TODO: move the ufo 1 pixel in the x direction (and 0 in the y direction)
def move_ufo(ufo, x):
    (oval1, oval2) = ufo
    x+= 1
    print(x)

    if x >= 300:
        oval1.move(-300,0)
        oval2.move(-300,0)

    else:
        oval1.move(1,0)
        oval2.move(1,0)
        x = 0z

    return x
    # (oval1, oval2) = ufo
    # oval1.move(1,0)
    # oval2.move(1,0)

##### Main part of the script ######


# creates a (300, 300) size screen
# (0, 0) is the upper left corner
screen_width = 300
screen_height = 300
win = GraphWin('UFO', screen_width, screen_height)

# draw the sky, grass, and sun
draw_scenery()

x = 0 # keeps track of the x position of the UFO
ufo = draw_ufo()


# TODO: animate the UFO flying by looping through the code below forever!
# TODO: wait .01 second
# TODO: move the UFO
#
while True:
    time.sleep(.01)
    x = move_ufo(ufo,x)

    #
    # if x >= screen_width:
    #     oval1.move(-screen_width)
    #     oval2.move(-screen_width)

win.mainloop()
