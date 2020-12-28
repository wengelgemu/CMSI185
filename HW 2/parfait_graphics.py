'''
parfait_graphics.py
Name: Wengel Gemu
Collaborators:
Date: September 12, 2019
Desscription: Draws the ladyfinger parfait recipe
'''

from graphics import *

# create the graphics window
win = GraphWin("Ladyfinger Parfait", 300, 300)
win.setBackground("light blue")

# draws the ladyfinger parfait
def parfait_stamp(x, y):

    draw_parfait = Circle(Point(x, y), 30)
    draw_parfait.setFill("pink")
    draw_parfait.setOutline("beige")
    draw_ladyfinger = Oval(Point(x+20, y+5), Point(x-20, y-5))
    draw_ladyfinger.setFill("beige")
    draw_ladyfinger.setOutline("light blue")

    draw_parfait.draw(win)
    draw_ladyfinger.draw(win)

# call function for graphic
parfait_stamp(150, 230)

# draws the text for the ladyfinger recipie
def ladyfingers():
    ladyfingers = Text(Point(150, 90), "Ladyfingers: ")
    ladyfingers.setStyle("italic")
    ladyfingers.setSize(15)
    ladyfingers.setTextColor("purple")
    ladyfingers2 = Text(Point(150, 105), "* 6 eggs, separated")
    ladyfingers2.setSize(10)
    ladyfingers3 = Text(Point(150, 115), "* Melted butter, for brushing pan")
    ladyfingers3.setSize(10)

    ladyfingers.draw(win)
    ladyfingers2.draw(win)
    ladyfingers3.draw(win)

# draws the text for the parfait cream recipie
def parfait_cream(): 
    parfait = Text(Point(150, 135), "Parfait Cream:")
    parfait.setStyle("italic")
    parfait.setSize(15)
    parfait.setTextColor("purple")
    parfait2 = Text(Point(150, 150), "* 2 cups melted vanilla ice cream")
    parfait2.setSize(10)
    parfait3 = Text(Point(150, 160), "* 4 tablespoons orange flavored liqueur")
    parfait3.setSize(10)
    parfait4 = Text(Point(150, 170), "* 1 cup raspberries")
    parfait4.setSize(10)

    parfait.draw(win)
    parfait2.draw(win)
    parfait3.draw(win)
    parfait4.draw(win)


# draws the text for the ladyfinger parfait recipie borders and title header
def ladyfinger_parfait():
    border = Text(Point(150, 10), "------------*******<><><><><>oooooo<><><><>******-------------")
    border.setSize(10)
    border.setTextColor("beige")
    title = Text(Point(150, 30), "Ladyfinger Parfait")
    title.setSize(20)
    title.setStyle("bold")
    title.setTextColor("lavender")
    border2 = Text(Point(150, 50), "------------*******<><><><><>oooooo<><><><>******-------------")
    border2.setSize(10)
    border2.setTextColor("beige")
    ladyfingers()
    parfait_cream()
    border3 = Text(Point(150, 60), "------------*******<><><><><>oooooo<><><><>******-------------")
    border3.setSize(10)
    border3.setTextColor("beige")

    border.draw(win)
    title.draw(win)
    border2.draw(win)
    border3.draw(win)

# call function for text
ladyfinger_parfait()

# process events
win.mainloop()
