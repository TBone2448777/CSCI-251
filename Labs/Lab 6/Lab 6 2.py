import graphics
def main():
    win=graphics.GraphWin("A Quadratic Plot",600,600)
    for x in range(600):
        y=int(x**2/1200)
        win.plot(x,y,"blue")
main()
