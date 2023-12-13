import random
from graphics import *
from time import sleep

inHouse = True
inGreatRoom = False
inBedroom = False
inWaterCloset = False
mastersolved = False

def bedroomLock():
    a1 = False
    a2 = False
    a3 = False
    a4 = False
    a5 = False
    a6 = False
    b1 = False
    b2 = False
    b3 = False
    b4 = False
    b5 = False
    b6 = False
    c1 = False
    c2 = False
    c3 = False
    c4 = False
    c5 = False
    c6 = False
    d1 = False
    d2 = False
    d3 = False
    d4 = False
    d5 = False
    d6 = False
    e1 = False
    e2 = False
    e3 = False
    e4 = False
    e5 = False
    e6 = False
    run = True
    w=GraphWin("SQUARED GUIDE", 450, 400)
    rec = Rectangle(Point(0, 0), Point(450, 400))
    rec.draw(w)
    rec.setFill("white")
    rec.setOutline("white")
    guide = Text(Point(425, 25), "1")
    guide.draw(w)
    guide = Text(Point(425, 75), "1")
    guide.draw(w)
    guide = Text(Point(375, 75), "1")
    guide.draw(w)
    guide = Text(Point(325, 75), "1")
    guide.draw(w)
    guide = Text(Point(225, 75), "1")
    guide.draw(w)
    guide = Text(Point(175, 75), "3")
    guide.draw(w)
    guide = Text(Point(425, 125), "1")
    guide.draw(w)
    guide = Text(Point(375, 125), "3")
    guide.draw(w)
    guide = Text(Point(325, 125), "1")
    guide.draw(w)
    guide = Text(Point(275, 125), "5")
    guide.draw(w)
    guide = Text(Point(225, 125), "1")
    guide.draw(w)
    guide = Text(Point(175, 125), "1")
    guide.draw(w)
    guide = Text(Point(125, 175), "6")
    guide.draw(w)
    guide = Text(Point(75, 225), "1")
    guide.draw(w)
    guide = Text(Point(125, 225), "1")
    guide.draw(w)
    guide = Text(Point(75, 275), "3")
    guide.draw(w)
    guide = Text(Point(125, 275), "2")
    guide.draw(w)
    guide = Text(Point(125, 325), "3")
    guide.draw(w)
    guide = Text(Point(25, 375), "1")
    guide.draw(w)
    guide = Text(Point(75, 375), "1")
    guide.draw(w)
    guide = Text(Point(125, 375), "2")
    guide.draw(w)
    while run:
        choice = w.getMouse()
        #A Row
        if (150 < choice.getX() < 200) and (150 < choice.getY() < 200):
            if a1 == True:
                a1 = False
                rec = Rectangle(Point(150, 150), Point(200, 200))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                a1 = True
                rec = Rectangle(Point(150, 150), Point(200, 200))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (200 < choice.getX() < 250) and (150 < choice.getY() < 200):
            if a2 == True:
                a2 = False
                rec = Rectangle(Point(200, 150), Point(250, 200))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                a2 = True
                rec = Rectangle(Point(200, 150), Point(250, 200))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (250 < choice.getX() < 300) and (150 < choice.getY() < 200):
            if a3 == True:
                a3 = False
                rec = Rectangle(Point(250, 150), Point(300, 200))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                a3 = True
                rec = Rectangle(Point(250, 150), Point(300, 200))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (300 < choice.getX() < 350) and (150 < choice.getY() < 200):
            if a4 == True:
                a4 = False
                rec = Rectangle(Point(300, 150), Point(350, 200))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                a4 = True
                rec = Rectangle(Point(300, 150), Point(350, 200))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (350 < choice.getX() < 400) and (150 < choice.getY() < 200):
            if a5 == True:
                a5 = False
                rec = Rectangle(Point(350, 150), Point(400, 200))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                a5 = True
                rec = Rectangle(Point(350, 150), Point(400, 200))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (400 < choice.getX() < 450) and (150 < choice.getY() < 200):
            if a6 == True:
                a6 = False
                rec = Rectangle(Point(400, 150), Point(450, 200))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                a6 = True
                rec = Rectangle(Point(400, 150), Point(450, 200))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        #B ROW
        if (150 < choice.getX() < 200) and (200 < choice.getY() < 250):
            if b1 == True:
                b1 = False
                rec = Rectangle(Point(150, 200), Point(200, 250))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                b1 = True
                rec = Rectangle(Point(150, 200), Point(200, 250))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (200 < choice.getX() < 250) and (200 < choice.getY() < 250):
            if b2 == True:
                b2 = False
                rec = Rectangle(Point(200, 200), Point(250, 250))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                b2 = True
                rec = Rectangle(Point(200, 200), Point(250, 250))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (250 < choice.getX() < 300) and (200 < choice.getY() < 250):
            if b3 == True:
                b3 = False
                rec = Rectangle(Point(250, 200), Point(300, 250))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                b3 = True
                rec = Rectangle(Point(250, 200), Point(300, 250))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (300 < choice.getX() < 350) and (200 < choice.getY() < 250):
            if b4 == True:
                b4 = False
                rec = Rectangle(Point(300, 200), Point(350, 250))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                b4 = True
                rec = Rectangle(Point(300, 200), Point(350, 250))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (350 < choice.getX() < 400) and (200 < choice.getY() < 250):
            if b5 == True:
                b5 = False
                rec = Rectangle(Point(350, 200), Point(400, 250))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                b5 = True
                rec = Rectangle(Point(350, 200), Point(400, 250))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (400 < choice.getX() < 450) and (200 < choice.getY() < 250):
            if b6 == True:
                b6 = False
                rec = Rectangle(Point(400, 200), Point(450, 250))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                b6 = True
                rec = Rectangle(Point(400, 200), Point(450, 250))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        #Row D
        if (150 < choice.getX() < 200) and (300 < choice.getY() < 350):
            if d1 == True:
                d1 = False
                rec = Rectangle(Point(150, 300), Point(200, 350))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                d1 = True
                rec = Rectangle(Point(150, 300), Point(200, 350))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (200 < choice.getX() < 250) and (300 < choice.getY() < 350):
            if d2 == True:
                d2 = False
                rec = Rectangle(Point(200, 300), Point(250, 350))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                d2 = True
                rec = Rectangle(Point(200, 300), Point(250, 350))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (250 < choice.getX() < 300) and (300 < choice.getY() < 350):
            if d3 == True:
                d3 = False
                rec = Rectangle(Point(250, 300), Point(300, 350))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                d3 = True
                rec = Rectangle(Point(250, 300), Point(300, 350))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (300 < choice.getX() < 350) and (300 < choice.getY() < 350):
            if d4 == True:
                d4 = False
                rec = Rectangle(Point(300, 300), Point(350, 350))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                d4 = True
                rec = Rectangle(Point(300, 300), Point(350, 350))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (350 < choice.getX() < 400) and (300 < choice.getY() < 350):
            if d5 == True:
                d5 = False
                rec = Rectangle(Point(350, 300), Point(400, 350))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                d5 = True
                rec = Rectangle(Point(350, 300), Point(400, 350))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (400 < choice.getX() < 450) and (300 < choice.getY() < 350):
            if d6 == True:
                d6 = False
                rec = Rectangle(Point(400, 300), Point(450, 350))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                d6 = True
                rec = Rectangle(Point(400, 300), Point(450, 350))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        #Row E
        if (150 < choice.getX() < 200) and (350 < choice.getY() < 400):
            if e1 == True:
                e1 = False
                rec = Rectangle(Point(150, 350), Point(200, 400))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                e1 = True
                rec = Rectangle(Point(150, 350), Point(200, 400))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (200 < choice.getX() < 250) and (350 < choice.getY() < 400):
            if e2 == True:
                e2 = False
                rec = Rectangle(Point(200, 350), Point(250, 400))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                e2 = True
                rec = Rectangle(Point(200, 350), Point(250, 400))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (250 < choice.getX() < 300) and (350 < choice.getY() < 400):
            if e3 == True:
                e3 = False
                rec = Rectangle(Point(250, 350), Point(300, 400))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                e3 = True
                rec = Rectangle(Point(250, 350), Point(300, 400))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (300 < choice.getX() < 350) and (350 < choice.getY() < 400):
            if e4 == True:
                e4 = False
                rec = Rectangle(Point(300, 350), Point(350, 400))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                e4 = True
                rec = Rectangle(Point(300, 350), Point(350, 400))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (350 < choice.getX() < 400) and (350 < choice.getY() < 400):
            if e5 == True:
                e5 = False
                rec = Rectangle(Point(350, 350), Point(400, 400))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                e5 = True
                rec = Rectangle(Point(350, 350), Point(400, 400))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (400 < choice.getX() < 450) and (350 < choice.getY() < 400):
            if e6 == True:
                e6 = False
                rec = Rectangle(Point(400, 350), Point(450, 400))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                e6 = True
                rec = Rectangle(Point(400, 350), Point(450, 400))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        #Row C
        if (150 < choice.getX() < 200) and (250 < choice.getY() < 300):
            if c1 == True:
                c1 = False
                rec = Rectangle(Point(150, 250), Point(200, 300))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                c1 = True
                rec = Rectangle(Point(150, 250), Point(200, 300))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (200 < choice.getX() < 250) and (250 < choice.getY() < 300):
            if c2 == True:
                c2 = False
                rec = Rectangle(Point(200, 250), Point(250, 300))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                c2 = True
                rec = Rectangle(Point(200, 250), Point(250, 300))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (250 < choice.getX() < 300) and (250 < choice.getY() < 300):
            if c3 == True:
                c3 = False
                rec = Rectangle(Point(250, 250), Point(300, 300))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                c3 = True
                rec = Rectangle(Point(250, 250), Point(300, 300))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (300 < choice.getX() < 350) and (250 < choice.getY() < 300):
            if c4 == True:
                c4 = False
                rec = Rectangle(Point(300, 250), Point(350, 300))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                c4 = True
                rec = Rectangle(Point(300, 250), Point(350, 300))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (350 < choice.getX() < 400) and (250 < choice.getY() < 300):
            if c5 == True:
                c5 = False
                rec = Rectangle(Point(350, 250), Point(400, 300))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                c5 = True
                rec = Rectangle(Point(350, 250), Point(400, 300))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (400 < choice.getX() < 450) and (250 < choice.getY() < 300):
            if c6 == True:
                c6 = False
                rec = Rectangle(Point(400, 250), Point(450, 300))
                rec.draw(w)
                rec.setFill("white")
                rec.setOutline("white")
            else:
                c6 = True
                rec = Rectangle(Point(400, 250), Point(450, 300))
                rec.draw(w)
                rec.setFill("black")
                rec.setOutline("white")
        if (a1 == True and a2 == True and a3 == True and a4 == True and a5 == True and a6 == True and b1 == True and b2 == False and b3 == True and b4 == False and b5 == False and b6 == False and c1 == True and c2 == True and c3 == True and c4 == False and c5 == True and c6 == True and d1 == False and d2 == False and d3 == True and d4 == True and d5 == True and d6 == False and e1 == True and e2 == False and e3 == True and e4 == False and e5 == True and e6 == True):
            print("Success!")
            run = False

def squaredGuide():
    w=GraphWin("SQUARED GUIDE", 250, 200)
    a1 = Rectangle(Point(101, 51), Point(149, 99))
    a1.draw(w)
    a1.setFill("black")
    a3 = Rectangle(Point(201, 51), Point(249, 99))
    a3.draw(w)
    a3.setFill("black")
    b1 = Rectangle(Point(101, 101), Point(149, 149))
    b1.draw(w)
    b1.setFill("black")
    b2 = Rectangle(Point(151, 101), Point(199, 149))
    b2.draw(w)
    b2.setFill("black")
    b3 = Rectangle(Point(201, 101), Point(249, 149))
    b3.draw(w)
    b3.setFill("black")
    c2 = Rectangle(Point(151, 151), Point(199, 199))
    c2.draw(w)
    c2.setFill("black")
    guide = Text(Point(125, 25), "2")
    guide.draw(w)
    guide = Text(Point(175, 25), "2")
    guide.draw(w)
    guide = Text(Point(225, 25), "2")
    guide.draw(w)
    guide = Text(Point(25, 75), "1")
    guide.draw(w)
    guide = Text(Point(75, 75), "1")
    guide.draw(w)
    guide = Text(Point(75, 125), "3")
    guide.draw(w)
    guide = Text(Point(75, 175), "1")
    guide.draw(w)
    sleep(5)
    print("\n(Don't be afraid if the program seems to have timed out. It should still be visible.)")
    print("This seems to be a guide to a key of some sort.")

class House:
    def __init__(self):
        self.maps = [" ________________________________________________\n|         |      X             |                 |\n|  Great  |    Water Closet    |     Bedroom     |\n|  Room   |                    |                 |\n|         |________________0___|_____________0___|\n|         0               Hallway                |\n|_________|_________________________________0____|", " ________________________________________________\n|         |                    |        X        |\n|  Great  |     Bedroom        |   Water Closet  |\n|  Room   |                    |                 |\n|         |________________0___|_____________0___|\n|         0               Hallway                |\n|_________|_________________________________0____|"," ________________________________________________\n|         |      X             |                 |\n|  Water  |     Great Room     |     Bedroom     |\n|  Closet |                    |                 |\n|         |________________0___|_____________0___|\n|         0               Hallway                |\n|_________|_________________________________0____|"]
        self.labeledmaps = [" ________________________________________________\n|     3   |      X         2   |              2  |\n|  Great  |    Water Closet    |     Bedroom     |\n|  Room   |                    |          4      |\n|         |________________0___|_____________0___|\n|  1      0        6      Hallway                |\n|_________|_________________________________0____|", " ________________________________________________\n|     4   |                3   |        X     2  |\n|  Great  |     Bedroom        |   Water Closet  |\n|  Room   |                    |          6      |\n|         |________________0___|_____________0___|\n|  5      0        1      Hallway                |\n|_________|_________________________________0____|"," ________________________________________________\n|     6   |      X         4   |              5  |\n|  Water  |     Great Room     |     Bedroom     |\n|  Closet |                    |          3      |\n|         |________________0___|_____________0___|\n|  1      0        2      Hallway                |\n|_________|_________________________________0____|"]
        self.chosenMap = 0
        self.map=self.maps[self.chosenMap]
        self.labeledmap=self.labeledmaps[self.chosenMap]
        self.one = "A squirt gun full of acid"
        self.two = "A taser nerf gun"
        self.three = "A shoelace"
        self.four = "A pair of safety Scissors"
        self.five = "A plunger"
        self.six = "157 empty laxative boxes"
        if self.chosenMap == 0:
            self.left = "Great Room"
            self.leftone = self.two
            self.lefttwo = self.four
            self.middle = "Water Closet"
            self.middletwo = self.one
            self.right = "Bedroom"
            self.rightone = self.three
            self.righttwo = self.five
            self.body = self.middle
        if self.chosenMap == 1:
            self.left = "Great Room"
            self.leftone = self.four
            self.lefttwo = self.five
            self.middle = "Bedroom"
            self.lefttwo = self.three
            self.right = "Water Closet"
            self.leftone = self.two
            self.lefttwo = self.six
            self.body = self.right
        if self.chosenMap == 2:
            self.left = "Water Closet"
            self.leftone = self.six
            self.lefttwo = self.three
            self.middle = "Great Room"
            self.lefttwo = self.four
            self.right = "Bedroom"
            self.leftone = self.three
            self.lefttwo = self.five
            self.body = self.middle
        print("Angelo: The body is in the " + self.body.lower() + ".")
        sleep(2)
        print("Angelo: Oh... and also two of the doors have mysteriously locked. My \nbrother, Aaron, is locked behind one of the doors.")
        sleep(3)
    def showMap(self):
        print(self.map)
    def showTMap(self):
        print(self.labeledmap)
    def decideLocked(self):
        self.roomList = ["Great Room", "Bedroom", "Water Closet"]
        self.roomList.remove(self.body)
        unlockDecider = 0
        self.unlocked = self.roomList[unlockDecider]
        self.roomList.pop(unlockDecider)
        self.secondRoom = self.roomList[0]
        self.secondRoom = False
        self.allOpen = False
        self.done = False
        self.roomTwo = False
        self.bedLock = True
        self.battery = False
        self.wclock = False
    def explore(self):
        choice = input("\nWould you like to check the GREAT ROOM, BEDROOM, WATER CLOSET, or EXIT? ")
        if choice.lower() == "great room":
            if (self.unlocked == "Great Room") or (self.secondRoom == "Great Room" and self.roomTwo == True) or (self.allOpen == True):
                print("You enter the Great Room.")
                global inHouse
                inHouse = False
                global inGreatRoom
                inGreatRoom = True
            else:
                print("The door is locked.")
        if choice.lower() == "bedroom":
            if (self.roomTwo == True):
                inHouse = False
                global inBedroom
                inBedroom = True
            else:
                print("The door is locked.")
        if choice.lower() == "water closet":
            if (self.allOpen == True):
                inHouse = False
                global inWaterCloset
                inWaterCloset= True
            else:
                print("The door is locked.")
        if choice.lower() == "exit":
            if (self.done != True):
                print("\nAngelo: Wait! You can't leave yet! You haven't solved the murder!")
    def GreatRoom(self):
        if self.left == "Great Room":
            print("\nYou look around the room. The first thing that catches your \neye is " + self.leftone.lower() + " and " + self.lefttwo.lower() + ".")
            going = True
            while going:
                choice = input("\nWhat would you like to inspect first? \nThe " + self.leftone.upper() + ", " + self.lefttwo.upper() + " , THE TRASH CAN, \nmysterious PERSON standing in and facing the corner, or EXIT? ")
                if choice.lower() == self.leftone.lower():
                    print("\nThe taser nerf gun seems to no longer work. It seems to be out of charge. \nLooking at the area around it, it seems to have been used for pest control. \nDead rats litter the ground. But were they why the taser nerf gun was made? \nOr were they used to test its strength? The gun seems to be out of battery.")
                    sleep(7)
                    if self.battery:
                        print("You place the battery you found within the taser nerf gun. The prongs spark. The gun works once more.")
                        print("Erica: Oh! You fixed my nerf gun! Thank you! By the way, did you know there's a Mastermind lock on the Water Closet?")
                        self.allOpen = True
                if choice.lower() == self.lefttwo.lower():
                    print("\nThe safety scissors seem quite dull.")
                    sleep(2)
                if choice.lower() == "the trash can":
                    print("\nInside the trash can you find a slip of paper. Don't lose(close) it.")
                    squaredGuide()
                    self.roomTwo = True
                if choice.lower() == "person":
                    print("\nYou walk over to the mysterious hooded figure. You hear loud, raspy breathing.")
                    sleep(1)
                    print("\nYou: Hello!")
                    sleep(1)
                    print("\nThe hooded figure pulls the hood back, and below is a beautiful woman.")
                    sleep(3)
                    print("\nUnexpectedly Beautiful Woman: Hi... are you the P.I. my brother called?")
                    sleep(3)
                    print("\nYou: Yes. How may I refer to you? And how are you holding up?")
                    sleep(3)
                    print("\nUnexpectedly Beautiful Woman: You can call me Erica... not so well. \nI HATE HATE HATE rats. And I ran out of power.")
                    sleep(5)
                    print("\nYou begin to back away slowly.")
                    sleep(1)
                    print("\nYou: Okay... bye.")
                    sleep(1)
                    print("\nErica: Buh bye!")
                    sleep(1)
                    print("\nWell that was odd.")
                    sleep(4)
                if choice.lower() == "exit":
                    print("\nYou leave the room.")
                    going = False
                    global inHouse
                    inHouse = True
                    global inGreatRoom
                    inGreatRoom = False
    def Bedroom(self):
        if self.bedLock:
            print("The door is locked. Maybe I can open it.")
            bedroomLock()
            self.bedLock = False
        else:
            sleep(3)
            print("\nYou enter the Bedroom.")
            sleep(1)
            print("A few things jump out to you immediately, a shoelace lays\natop the king-sized bed and a plunger is in the corner of the room. \nA young couple is seated on the bed, watching as you enter. A \nbookshelf is against the left wall.")
            sleep(5)
            going = True
            while going:
                choice = input("\nWhat would you like to inspect? SHOELACE, PLUNGER, \nBOOKSHELF, or YOUNG COUPLE? Or EXIT? ")
                if choice.lower() == "shoelace":
                    print("\nYou walk to the shoelace. It seems stretched and is \nfraying a bit. There's a bit of red tinging the edges. It looks familiar.")
                if choice.lower() == "plunger":
                    print("\nUpon inspecting the plunger, it seems like it has been \nused recently for a non-manufactorer-condoned purpose. Ew.")
                if choice.lower() == "young couple":
                    print("\nSeated woman: Hello! Sir! We're so glad you showed up. \nWe've been stuck in here for hours. The doors just suddenly locked. \nYou know how it is. It's a Wednesday!")
                    sleep(6)
                    print("\nYou: Wait, what? I don't know how it is either, it's \nbizarre. Is this normal for you? Also, it's Monday. Are you cra--- \nnevermind.")
                    sleep(5)
                    print("\nSeated Man: Don't misunderstand our excitement. Jenny \nand I are just so excited to be free. The name's Luther by the way.")
                    sleep(5)
                    print("\nYou: May I ask you two some questions?")
                    sleep(2)
                    questioning = True
                    while questioning:
                        question = input("\nWhat would you like to ask? WHO are you to Angelo's father? WHY were you in here during the murder? THOUGHTS on Angelo's father? EXIT? ")
                        if question.lower() == "why":
                            print("\nLuther: We were... *winks twice*")
                            sleep(2)
                            print("\nJenny: Shut up, Luther. We were actually just reading and keeping to our own devices.")
                            sleep(2)
                            print("As she finished that statement she sends a glare in Luther's direction.")
                            sleep(2)
                        if question.lower() == "who":
                            print("\nJenny: I'm his daughter. Luther is just my fiance.")
                            sleep(2)
                            print("\nLuther: Just? *said in playful manner*")
                            sleep(2)
                        if question.lower() == "thoughts":
                            print("\nLuther: I always really liked the guy. I admired \nhim, but I didn't know him as well as I wish I did.")
                            sleep(3)
                            print("\nJenny: My dad didn't really like him. It wasn't \nLuther's fault, he just didn't think anybody would be good enough \nfrom me. He might not have liked Luther, but he did approve \nof him though.")
                            sleep(5)
                        if question.lower() == "exit":
                            print("\nYou: Okay, thanks you two. This was very helpful.")
                            questioning = False
                if choice.lower() == "bookshelf":
                    sleep(2)
                    read = input("\nYou scan the shelves, seeing nothing amiss. Would you like to read something? Y/N? ")
                    sleep(3)
                    if read.lower() == "y":
                        book = input("\nWhat would you like to read? PRIDE AND PREJUDICE AND ZOMBIES, ABE LINCOLN: VAMPIRE HUNTER, WEDNESDAY: A DAY: THE MEMOIR: FOR THE ELDERLY, or something else? ")
                        sleep(3)
                        if book.upper() == "WEDNESDAY: A DAY: THE MEMOIR: FOR THE ELDERLY":
                              print("\nUpon grabbing the book a secret compartment opens up. It's a battery! You pocket it.")
                              self.battery = True
                        else:
                            print("\nYou begin to read " + book + " and it isn't long before you finish. What a good book!")
                if choice.lower() == "exit":
                    print("\nYou leave the room.")
                    going = False
                    global inHouse
                    inHouse = True
                    global inBedroom
                    inBedroom = False
    def WaterCloset(self):
        if self.allOpen:
            if self.wclock:
                print(test)
            else:
                mastermind()
                global mastersolved
                self.wclock = mastersolved
            
def phoneCall():
    print("RING RING RING")
    sleep(0.5)
    print("*Click*")
    sleep(1)
    print("You: Rent-a-P.I., how may I help you?")
    sleep(1.5)
    print("Mysterious Voice: There's been a murder!")
    sleep(1.5)
    print("You: I'm on my way!\n")
    sleep(2)
    transport = True
    while transport:
        transport = input("What method of transportation do you take? MOTORCYCLE or CAR? ").upper()
        if transport == "MOTORCYCLE":
            vehicle = "motorcycle"
            transport = False
        if transport == "CAR":
            vehicle = "car"
            transport = False
    sleep(2)
    print("\nYour " + vehicle + " speeds out of your garage, kicking up plumes \nof dust in its wake. You arrive at the house, breaking just\nin time to avoid crashing through their garage.")
    sleep(5)
    return vehicle

def arrival():
    print("You walk up to the front door, nearly slipping on your shoe that recently lost much of its tightness. *Knock Knock*")
    sleep(3)
    print("The door whips open.")
    sleep(1)
    print("\nShort Man: Hello! P.I.? I never got your name, how should I address you?")
    sleep(2)
    name = input("\nWhat is your name? ")
    sleep(1)
    print("\nYou: You may call me " + name + ". What happened here?")
    sleep(2.5)
    print("\nShort Man: You didn't ask my name? How rude!? You can call me Angelo.")
    sleep(2)
    print("Angelo: I was lounging by the fire, watching a TV show, and I heard\na shout from the other room. Upon investigating I found my father,\nlying there, dead.")
    sleep(5)

def house():
    print("\nYou walk into the house and begin to survey the building before\nquickly sketching a map.")
    h = House()
    type(h)
    h.showMap()
    h.showTMap()
    h.decideLocked()
    playing = True
    while playing:
        while inHouse:
            h.explore()
        while inGreatRoom:
            h.GreatRoom()
        while inBedroom:
            h.Bedroom()
        while inWaterCloset:
            h.WaterCloset()

def mastermind():
    master=GraphWin("MASTERMIND", 1000, 512)
    gameStart = True
    while gameStart:
        boardClear = Rectangle(Point(0,0), Point(1000, 512))
        boardClear.draw(master)
        boardClear.setFill("white")
        boardClear.setOutline("white")
        header = Rectangle(Point(0,0), Point(500, 32))
        header.draw(master)
        header.setFill("gray")
        header.setOutline("gray")
        splitter = Line(Point(500,0), Point(500, 512))
        splitter.draw(master)
        splitter.setFill("black")
        splitter.setOutline("black")
        div1 = Line(Point(100,0), Point(100,512))
        div1.draw(master)
        div2 = Line(Point(400,0), Point(400,512))
        div2.draw(master)
        for i in range(32,500, 40):
            div3 = Line(Point(0,i), Point(500,i))
            div3.draw(master)
        colorList = ["green", "blue", "red", "yellow", "purple", "orange"]
        colorCount = 0
        for i in range(522, 950, 76):
            colorSquare = Rectangle(Point(i,414), Point(i+76, 490))
            colorSquare.draw(master)
            colorSquare.setFill(colorList[colorCount])
            colorSquare.setOutline("black")
            colorCount += 1
        guessText = Text(Point(50, 16), "Guess")
        guessText.draw(master)
        guessText = Text(Point(250, 16), "Colors")
        guessText.draw(master)
        guessText = Text(Point(450, 16), "Correct")
        guessText.draw(master)
        guessNumber = 1
        for i in range(52, 512, 40):
            guessText = Text(Point(50, i), guessNumber)
            guessText.draw(master)
            guessNumber += 1
        for i in range(560, 900, 95):
            colorSquare = Rectangle(Point(i,22), Point(i+95, 370))
            colorSquare.draw(master)
        guessTrack = 0
        gameContinue = True
        string = "GBRYPO"
        import random
        code = ""
        for i in range(0,4):
            code += string[random.randint(0,len(string)-1)]
        while gameContinue:
            guess = ""
            for i in range(560, 900, 95):
                unassigned = True
                while (unassigned == True):
                    clickOne = master.getMouse()
                    if ((490 > clickOne.getY() > 414) and gameStart == True):
                        if (522 < clickOne.getX() < 598):
                            guess += "G"
                            colorSquare = Rectangle(Point(i,22), Point(i+95, 370))
                            colorSquare.draw(master)
                            colorSquare.setFill("green")
                            colorSquare.setOutline("green")
                            unassigned = False
                        if (598 < clickOne.getX() < 674):
                            guess += "B"
                            colorSquare = Rectangle(Point(i,22), Point(i+95, 370))
                            colorSquare.draw(master)
                            colorSquare.setFill("blue")
                            colorSquare.setOutline("blue")
                            unassigned = False
                        if (674 < clickOne.getX() < 750):
                            guess += "R"
                            colorSquare = Rectangle(Point(i,22), Point(i+95, 370))
                            colorSquare.draw(master)
                            colorSquare.setFill("red")
                            colorSquare.setOutline("red")
                            unassigned = False
                        if (750 < clickOne.getX() < 826):
                            guess += "Y"
                            colorSquare = Rectangle(Point(i,22), Point(i+95, 370))
                            colorSquare.draw(master)
                            colorSquare.setFill("yellow")
                            colorSquare.setOutline("yellow")
                            unassigned = False
                        if (826 < clickOne.getX() < 902):
                            guess += "P"
                            colorSquare = Rectangle(Point(i,22), Point(i+95, 370))
                            colorSquare.draw(master)
                            colorSquare.setFill("purple")
                            colorSquare.setOutline("purple")
                            unassigned = False
                        if (902 < clickOne.getX() < 978):
                            guess += "O"
                            colorSquare = Rectangle(Point(i,22), Point(i+95, 370))
                            colorSquare.draw(master)
                            colorSquare.setFill("orange")
                            colorSquare.setOutline("orange")
                            unassigned = False
            time.sleep(0.5)
            for i in range(560, 900, 95):
                colorSquare = Rectangle(Point(i,22), Point(i+95, 370))
                colorSquare.draw(master)
                colorSquare.setFill("white")
            counter = 0
            if (len(guess)==len(code)):
                for i in range(0, len(guess)):
                    if (guess[i] == code[i]):
                        counter += 1
            else:
                counter = -1
            numcorrect = counter
            tracker = guessTrack
            correctNum = numcorrect
            for i in range(0, 4):
                if (guess[i] == "G"):
                    colorBlock = Rectangle(Point(100 + (i * 75), 32 + (tracker*40)), Point(175 + (i * 75), 72 + (tracker*40)))
                    colorBlock.draw(master)
                    colorBlock.setFill("green")
                if (guess[i] == "B"):
                    colorBlock = Rectangle(Point(100 + (i * 75), 32 + (tracker*40)), Point(175 + (i * 75), 72 + (tracker*40)))
                    colorBlock.draw(master)
                    colorBlock.setFill("blue")
                if (guess[i] == "R"):
                    colorBlock = Rectangle(Point(100 + (i * 75), 32 + (tracker*40)), Point(175 + (i * 75), 72 + (tracker*40)))
                    colorBlock.draw(master)
                    colorBlock.setFill("red")
                if (guess[i] == "Y"):
                    colorBlock = Rectangle(Point(100 + (i * 75), 32 + (tracker*40)), Point(175 + (i * 75), 72 + (tracker*40)))
                    colorBlock.draw(master)
                    colorBlock.setFill("yellow")
                if (guess[i] == "P"):
                    colorBlock = Rectangle(Point(100 + (i * 75), 32 + (tracker*40)), Point(175 + (i * 75), 72 + (tracker*40)))
                    colorBlock.draw(master)
                    colorBlock.setFill("purple")
                if (guess[i] == "O"):
                    colorBlock = Rectangle(Point(100 + (i * 75), 32 + (tracker*40)), Point(175 + (i * 75), 72 + (tracker*40)))
                    colorBlock.draw(master)
                    colorBlock.setFill("orange")
            correctText = Text(Point(450, 52 + tracker * 40), correctNum)
            correctText.draw(master)
            guessTrack += 1
            if (numcorrect == 4):
                time.sleep(3)
                boardClear = Rectangle(Point(0,0), Point(1000, 512))
                boardClear.draw(master)
                boardClear.setFill("white")
                boardClear.setOutline("white")
                winNotif = Text(Point(500, 150), "CONGRATULATIONS! YOU WIN!")
                winNotif.draw(master)
                global mastersolved
                mastersolved = True
                print("SUCCESS!")
                gamecontinue = False
            if (guessTrack == 12):
                gameContinue = False
                boardClear = Rectangle(Point(0,0), Point(1000, 512))
                boardClear.draw(master)
                boardClear.setFill("white")
                boardClear.setOutline("white")
                askAgain = Text(Point(500, 200), "Would you like to play again?")
                askAgain.draw(master)
                boardClear = Rectangle(Point(0,226), Point(1000, 369))
                boardClear.draw(master)
                boardClear.setFill("green")
                boardClear.setOutline("green")
                boardClear = Rectangle(Point(0,369), Point(1000, 512))
                boardClear.draw(master)
                boardClear.setFill("red")
                boardClear.setOutline("red")
                choice = master.getMouse()
                if (369 < choice.getY() < 512):
                    gameStart = False
                    boardClear = Rectangle(Point(0,0), Point(1000, 512))
                    boardClear.draw(master)
                    boardClear.setFill("white")
                    boardClear.setOutline("white")

def main():
    vehicle = phoneCall()
    name = arrival()
    house()
    mastermind()

main()
