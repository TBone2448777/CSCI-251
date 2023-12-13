from random import randrange

class MSDie:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value=randrange(1, self.sides+1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        
    def getSides(self):
        return self.sides
    
    def newSides(self, newSides):
        self.sides = newSides

def main():
    print("\nWelcome to the alley! Here you guess what number my die will roll. You can choose how many sides there are, any number works. If you guess correctly you get three dollars, but every guess costs a dollar. Just reply with 'no' when I ask for your guess if you get tired of playing.\n")
    sideAmount = int(input("How many sides would you like the die to have? "))
    if sideAmount < 4:
        print("Sorry, that's too low! I have set it to four.\n")
        sideAmount = 4
    else:
        print("\n")
    winnings = 0
    a = MSDie(sideAmount)
    type(a)
    a.getSides()
    playing = True
    while playing:
        a.roll()
        roll = a.getValue()
        guess = input("What number do you think I'll roll? ")
        if ("no" == guess):
            playing = False
            print("Thanks for playing! Your ending balance was $" + str(winnings) + "!")
            break
        if (int(guess) == roll):
            winnings += 3
            print("Correct! I've added $3 to your account. You now have $" + str(winnings) + "\n")
        else:
            winnings += -1
            print("\nWrong! It was actually " + str(roll) + ". I've taken $1 from  your account. You now have $" + str(winnings) + "\n")
main()
