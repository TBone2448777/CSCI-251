def importDNA():
    infile = open("salmonella_genome.fna", "r")
    totalDNA = ""
    infile.readline()
    totalString = infile.read()
    totalString = totalString.replace("\n", "")
    return totalString

def mostCommonClose(importDNA, key):
    appearList = {}
    length = len(key)
    matches = 0
    for i in range(0, len(importDNA) - len(key)):
        checking = importDNA[i : i + length]
        amountWrong = 0
        for j in range (0, len(checking)):
            if (checking[j] != key[j]):
                amountWrong += 1
        if (amountWrong <= 1):
            if checking not in appearList:
                appearList[checking] = 1
            else:
                appearList[checking] += 1
    newDict = {}
    for key, value in appearList.items():
        newDict[value] = key
    for num in newDict:
        for i in appearList:
            if (num == appearList[i]):
                if (newDict[num] != i):
                    newDict[num] = newDict[num] + ", " + i
    newList = sorted(newDict, reverse = True)
    finDict = {}
    for appearances in newList:
        finDict[appearances] = newDict[appearances]
    for appearances in finDict:
        amount = finDict[appearances].count(",")
        if amount > 1:
            if appearances > 1:
                print("The strings " + finDict[appearances] + " appear " + str(appearances) + " times.")
            if appearances <= 1:
                print("The strings " + finDict[appearances] + " appear " + str(appearances) + " time.")
        else:
            if appearances > 1:
                print("The string " + finDict[appearances] + " appears " + str(appearances) + " times.")
            if appearances <= 1:
                print("The string " + finDict[appearances] + " appeared " + str(appearances) + " time.")

def main():
    search1 = "TGATG"
    search2 = "CTCTTGATC"
    stringDNA = importDNA()
    mostCommonClose(stringDNA, search2)
main()
