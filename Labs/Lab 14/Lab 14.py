def invert(dictionary):
    newdict = {}
    for key, value in dictionary.items():
        newdict[value] = key
    return newdict

def historyOne():
    events = {"Huns invade Europe":375, "Arabs invade Spain":711, "Hundred year war begins":1338}
    events["Spanish Armada defeated"] = 1588
    print(events.keys())
    print(events.values())

def movieOne():
    events = {"Get Out":1, "Chronicle":2, "Tucker and Dale vs. Evil":3, "Straight Up":4}
    test = invert(events)
    print(test)

def wordList():
    book = open("neverletmego2.txt", "r")
    bookWritten = book.read()
    bookWritten = bookWritten.lower()
    bookWritten = bookWritten.replace(".", " ")
    bookWritten = bookWritten.replace(",", " ")
    bookWritten = bookWritten.replace("?", " ")
    bookWritten = bookWritten.replace("!", " ")
    bookWritten = bookWritten.replace('"', " ")
    bookWritten = bookWritten.replace(";", " ")
    bookWritten = bookWritten.replace(":", " ")
    bookWritten = bookWritten.replace("-", " ")
    bookWritten = bookWritten.replace("\n", " ")
    bookWritten = bookWritten.replace("\t", " ")
    bookList = bookWritten.split()
    bookDict = {}
    bookOrder = []
    for i in range(400, 0, -1):
        for j in range(0, len(bookList)):
            item = bookList[j]
            amount = bookList.count(item)
            if (amount == i):
                bookDict[item] = amount
                if item not in bookOrder:
                    bookOrder.append(item)
    for i in range(0, len(bookDict)):
        print('The word "' + str(bookOrder[i]) + '" appears ' + str(bookDict[bookOrder[i]]) + " times.")
    print("Done")

def main():
    wordList()

main()
