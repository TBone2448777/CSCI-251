arrayX = 11
arrayY = 11

def importFile():
    infile = open("numbers.txt", "r")
    file = infile.read()
    return file

def printer(file):
    wholeList = file.split()
    for i in range(0, arrayY):
        for j in range(0, arrayX):
            if ((i != arrayY - 1) & (j != arrayX - 1)):
                number = wholeList[(i*10) + j]
                if (len(number) < 2):
                    number += " "
                print(number, end = " ")
        print("")

def printerWhile(file):
    wholeList = file.split()
    trackerY = 0
    while (trackerY != arrayY):
        trackerX = 0
        while(trackerX != arrayX):
            if ((trackerY != arrayY - 1) & (trackerX != arrayX - 1)):
                number = wholeList[(trackerY*10) + trackerX]
                if (len(number) < 2):
                    number += " "
                print(number, end = " ")
            trackerX += 1
        print("")
        trackerY += 1

def printerAverages(file):
    wholeList = file.split()
    trackerY = 0
    avg = 0
    while (trackerY != arrayY - 1):
        trackerX = 0
        avg += int(wholeList[trackerY*10])
        trackerY += 1
    print(int(avg) / trackerY)

def diagonalPrinter(file):
    wholeList = file.split()
    trackerY = 0
    avg = 0
    while (trackerY != arrayY - 1):
        number = int(wholeList[(trackerY*10) + trackerY])
        avg += number
        trackerY += 1
    print(int(avg)/trackerY)
    
def main():
    numList = importFile()
    printer(numList)
    printerWhile(numList)
    printerAverages(numList)
    print("")
    diagonalPrinter(numList)
main()
