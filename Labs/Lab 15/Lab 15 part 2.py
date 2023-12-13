def alphabetCounter(document, alphabet):
    infile = open(document, "r")
    doc = infile.read()
    countDict = {}
    for i in range(0, len(alphabet)):
        letter = alphabet[i]
        amount = doc.count(letter)
        countDict[letter] = amount
    return(countDict)

def ratiomaker(counted, alphabet):
    totalLetterCount = 0
    for i in range(0, len(alphabet)):
        totalLetterCount += counted[alphabet[i]]
    ratioDict = {}
    for i in range(0, len(alphabet)):
        ratioDict[alphabet[i]] = round((counted[alphabet[i]]/totalLetterCount)*100, 2)
    return(ratioDict)

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    wordleCount = alphabetCounter("wordle_words.txt", alphabet)
    nlmgCount = alphabetCounter("neverletmego.txt", alphabet)
    wordleRatio = ratiomaker(wordleCount, alphabet)
    nlmgRatio = ratiomaker(nlmgCount, alphabet)
    for i in range(0, len(alphabet)):
        print('The letter "' + alphabet[i] + '" appears ' + str(wordleRatio[alphabet[i]]) + '% of the time in the Wordle list and ' + str(nlmgRatio[alphabet[i]]) + '% of the time in the Never Let Me Go book.')
main()
