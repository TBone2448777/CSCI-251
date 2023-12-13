import graphics
def main():
    win=graphics.GraphWin("Mr. Morale and the Big Window",600,600)
    for x in range(300):
        y=x
        win.plot(x*2,y,"blue")
        win.plot(x*2+1, y, "blue")
main()
