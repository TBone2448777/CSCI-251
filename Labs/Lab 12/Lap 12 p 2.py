import random
def listGen():
    outfile = open("CATlist.txt", "w")
    charList = ["G", "C", "T", "A"]
    for i in range(0, 5):
        for j in range(0, 20):
            char = charList[random.randint(0, 3)]
            print(char, end = "", file = outfile)
        print("", file = outfile)
def searchCAT():
    infile = open("CATlist.txt", "r")
    combinedString = ""
    trackVal = 0
    for i in range(0, 5):
        workingLine = infile.readline()
        combinedString += workingLine
    combinedString = combinedString.replace("\n", "")
    for j in range(0, len(combinedString)):
        if (combinedString[j:3+j] == "CAT"):
            trackVal += 1
    print(trackVal)
def main():
    listGen()
    searchCAT()
main()
