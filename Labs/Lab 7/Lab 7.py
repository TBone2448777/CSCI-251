from graphics import *
def main():
    colors = ["white", "black", "blue", "red", "yellow"]
    w=GraphWin()
    w.setBackground("Orange")
    for i in range(0, 5):
        ws = Circle(Point(100, 100), 75 - (i*15))
        ws.draw(w)
        ws.setFill(colors[i])
        ws.setOutline(colors[i])
main()
