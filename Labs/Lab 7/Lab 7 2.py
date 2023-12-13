from graphics import *
def main():
    w=GraphWin("TRIANGLE MAKER", 400, 400)
    w.setBackground("Orange")
    p1 = w.getMouse()
    p2 = w.getMouse()
    p3 = w.getMouse()
    t = Polygon(p1, p2, p3)
    t.draw(w)
    color = input("What color would you like the triangle to be? ")
    t.setFill(color)
    t.setOutline(color)
main()
