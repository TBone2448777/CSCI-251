def forPrinter():
    infile = open("numbers.txt", "r")
    for line in infile:
        print(line, end = "")

def whilePrinter():
    infile = open("numbers.txt", "r")
    line = infile.readline()
    while line != "":
        print(line, end = "")
        line = infile.readline()

def whilePrinterAvg():
    summer = 0
    divider = 0
    infile = open("numbers.txt", "r")
    line = infile.readline()
    while line != "":
        holder = line.split()
        holderChooser = holder[0]
        summer += int(holderChooser)
        divider += 1
        line = infile.readline()
    if divider != 0:
        print(summer/divider)
    else:
        print("ERROR")
        
def whilePrinterAvgDiag():
    summer = 0
    divider = 0
    placer = 0
    infile = open("numbers.txt", "r")
    line = infile.readline()
    while line != "":
        holder = line.split()
        holderChooser = holder[placer]
        summer += int(holderChooser)
        divider += 1
        placer += 1
        line = infile.readline()
    if divider != 0:
        print(summer/divider)
    else:
        print("ERROR")
    
def main():
    print("\n")
    forPrinter()
    print("\n")
    whilePrinter()
    print("\n")
    whilePrinterAvg()
    print("\n")
    whilePrinterAvgDiag()

main()
