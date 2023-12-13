from graphics import *
import time
master=GraphWin("MASTERMIND", 1000, 512)
def createcode():
    string = "GBRYPO"
    import random
    code = ""
    for i in range(0,4):
        code += string[random.randint(0,len(string)-1)]
    return code

def comparestrings(guess, code):
    counter = 0
    if (len(guess)==len(code)):
        for i in range(0, len(guess)):
            if (guess[i] == code[i]):
                counter += 1
    else:
        counter = -1
    return counter

def drawBoard():
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

def sidebarFill(guess, tracker, correctNum):
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
def main():
    gameStart = True
    while gameStart:
        drawBoard()
        guessTrack = 0
        gameContinue = True
        code = createcode()
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
            numcorrect = comparestrings(guess, code)
            sidebarFill(guess, guessTrack, numcorrect)
            guessTrack += 1
            if (numcorrect == 4):
                time.sleep(3)
                boardClear = Rectangle(Point(0,0), Point(1000, 512))
                boardClear.draw(master)
                boardClear.setFill("white")
                boardClear.setOutline("white")
                winNotif = Text(Point(500, 150), "CONGRATULATIONS! YOU WIN!")
                winNotif.draw(master)
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
                choice = w.getMouse()
                if (369 < choice.getY() < 512):
                    gameStart = False
                    boardClear = Rectangle(Point(0,175), Point(1000, 512))
                    boardClear.draw(master)
                    boardClear.setFill("white")
                    boardClear.setOutline("white")
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
                choice = w.getMouse()
                if (369 < choice.getY() < 512):
                    gameStart = False
                    boardClear = Rectangle(Point(0,0), Point(1000, 512))
                    boardClear.draw(master)
                    boardClear.setFill("white")
                    boardClear.setOutline("white")
main()
