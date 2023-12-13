def importDNA():
    infile = open("salmonella_genome.fna", "r")
    totalDNA = ""
    infile.readline()
    totalString = infile.read()
    totalString = totalString.replace("\n", "")
    return totalString

def amountCount(importDNA):
    countG = 0
    countA = 0
    countC = 0
    countT = 0
    for i in range(0, len(importDNA)):
        if (importDNA[i] == "G"):
            countG += 1
        if (importDNA[i] == "A"):
            countA += 1
        if (importDNA[i] == "C"):
            countC += 1
        if (importDNA[i] == "T"):
            countT += 1
    print("There are " + str(countG) + " Gs, " + str(countA) + " As, " + str(countC) + " Cs, and " + str(countT) + " Ts.")

def searcher(importDNA, key):
    length = len(key)
    matches = 0
    for i in range(0, len(importDNA) - len(key)):
        if (importDNA[i : i + length] == key):
            matches += 1
    return matches

def closeSearcher(importDNA, key):
    length = len(key)
    matches = 0
    for i in range(0, len(importDNA)- len(key)):
        checking = importDNA[i : i + length]
        amountWrong = 0
        for j in range (0, len(checking)):
            if (checking[j] != key[j]):
                amountWrong += 1
        if (amountWrong <= 1):
            matches += 1
    return matches

def mostCommonClose(importDNA, key):
    appearList = []
    length = len(key)
    matches = 0
    for i in range(0, len(importDNA) - len(key)):
        checking = importDNA[i : i + length]
        amountWrong = 0
        for j in range (0, len(checking)):
            if (checking[j] != key[j]):
                amountWrong += 1
        if (amountWrong <= 1):
            appearList.append(checking)
    mostCommon = ""
    mostCommonCount = 0
    secondMostCommon = ""
    secondMostCommonCount = 0
    for i in range(0, len(appearList)):
        amountAppeared = appearList.count(appearList[i])
        if (appearList[i] != mostCommon) & (amountAppeared > mostCommonCount):
            mostCommonCount = amountAppeared
            mostCommon = appearList[i]
        else:
            if (appearList[i] != secondMostCommon) & (amountAppeared > secondMostCommonCount) & (appearList[i] != mostCommon):
                secondMostCommonCount = amountAppeared
                secondMostCommon = appearList[i]
    print(str(mostCommon) + " appears most, " + str(mostCommonCount) + " times.")
    print(str(secondMostCommon) + " appears second most, " + str(secondMostCommonCount) + " times.")

def main():
    search1 = "TGATG"
    search2 = "CTCTTGATC"
    stringDNA = importDNA()
    print("The length of the string is " + str(len(stringDNA)) + " characters long.")
    amountCount(stringDNA)
    print("The sequence " + str(search1) + " occurs " + str(searcher(stringDNA, search1)) + " times.")
    print("The sequence " + str(search2) + " occurs " + str(searcher(stringDNA, search2)) + " times.")
    print("A sequence one nucleobase from " + str(search2) + " occurs " + str(closeSearcher(stringDNA, search2)) + " times.")
    mostCommonClose(stringDNA, search2)
main()
