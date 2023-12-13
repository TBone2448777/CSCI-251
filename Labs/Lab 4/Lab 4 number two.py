def main():
    #Getting number
    number = int(input("What number would you like to use? "))
    #Loop 5 times
    for x in range(0, 5):
        #Squaring number by itself
        number = number ** 2
        #Printing new number
        print(number)
main()
