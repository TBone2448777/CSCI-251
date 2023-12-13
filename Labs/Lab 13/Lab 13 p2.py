def importFile():
    infile = open("neverletmego.txt", "r")
    file = infile.read()
    return file

def main():
    book = importFile()
    sentenceCounter = 0
    for i in range(0, len(book)):
        if book[i] == ".":
            sentenceCounter += 1
        if book[i] == "!":
            sentenceCounter += 1
        if book[i] == "?":
            sentenceCounter += 1
        if book[i:i+3] == "Mr.":
            sentenceCounter += -1
        if book[i:i+3] == "Ms.":
            sentenceCounter += -1
        if book[i:i+4] == "Mrs.":
            sentenceCounter += -1
        if book[i:i+3] == "Dr.":
            sentenceCounter += -1
        if book[i:i+4] == "www.":
            sentenceCounter += -1
        if book[i:i+4] == ".com":
            sentenceCounter += -1
        if book[i:i+4] == ".net":
            sentenceCounter += -1
        if book[i:i+4] == ".gov":
            sentenceCounter += -1
        if book[i:i+3] == "...":
            sentenceCounter += -3
        if book[i:i+3] == "Blvd.":
            sentenceCounter += -1
        if book[i:i+3] == "Ave.":
            sentenceCounter += -1
        if book[i:i+3] == "St.":
            sentenceCounter += -1
        if book[i:i+3] == "Prof.":
            sentenceCounter += -1
    print(sentenceCounter)

main()
