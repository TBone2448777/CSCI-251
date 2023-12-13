def main():
    DNAstring = input("What DNA string would you like to analyze? ").upper()
    DNAsequence = input("What sequence would you like to check for appearances? ").upper()
    numA = 0
    numC = 0
    numG = 0
    numT = 0
    for i in range(0, len(DNAstring)): #Increases counts of each letter
        if (DNAstring[i] == "A"):
            numA += 1
        if (DNAstring[i] == "C"):
            numC += 1
        if (DNAstring[i] == "G"):
            numG += 1
        if (DNAstring[i] == "T"):
            numT += 1
    print("There are " + str(numA) + " As, " + str(numC) + " Cs, " + str(numG) + " Gs, and " + str(numT) + " Ts.") #Tells amount of each letter
    print("Does " + str(DNAsequence) + " appear?") #Poses Question
    appearOrNo = False #Variable preparation for if statement below
    amountAppear = 0
    for x in range(len(DNAstring)): #Loop to check chunks of certain length to see if they match sequence
        if (DNAstring[x:x+len(DNAsequence)] == DNAsequence):
            appearOrNo = True
            amountAppear += 1
    if (appearOrNo == True): #Tells user that if it does, how many times it appears
        print("Yes! It appears " + str(amountAppear) + " times!")
    else:
        print("That sequence does not appear in the DNA string.")
main()
