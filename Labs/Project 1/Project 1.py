from graphics import *
def main():
    import random
    current = Point(400, 300)
    stepChoice = [-2, 2]
    newX = 0
    newY = 0
    color = ["cyan", "orange", "red", "yellow", "white", "pink"]
    w = GraphWin("Random Walk", 800, 600)
    w.setBackground("black")
    current.draw(w)
    p1 = Point(602, 148)
    p2 = Point(198, 148)
    p3 = Point(602, 454)
    p4 = Point(198, 454)
    line1 = Line(p1, p2)
    line1.setOutline(random.choice(color))
    line2 = Line(p3, p4)
    line2.setOutline(random.choice(color))
    line3 = Line(p2, p4)
    line3.setOutline(random.choice(color))
    line4 = Line(p1, p3)
    line4.setOutline(random.choice(color))
    line1.draw(w)
    line2.draw(w)
    line3.draw(w)
    line4.draw(w)
    for i in range(10000):
        dx = random.choice(stepChoice)
        dy = random.choice(stepChoice)
        if current.getX() + dx >= 200 and current.getX() + dx <= 600:
            newX = current.getX() + dx
        else:
            if current.getX() + dx <= 400:
                newX = current.getX()+2
            else:
                newX = current.getX()-2
        if current.getY() + dy >= 150 and current.getY() + dx <= 450:
            newY = current.getY() + dy
        else:
            if current.getY() + dy <= 300:
                newY = current.getY()+2
            else:
                newY = current.getY()-2
        nextPt=Point(newX, newY)
        line = Line(current,nextPt)
        line.setOutline(random.choice(color))
        line.draw(w)
        current=nextPt
main()
