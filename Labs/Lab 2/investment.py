# File: investment.py
# A simple program illustrating compounded interest
def main():
    print("Value of a 10-year investment at variable interest")
    rate = float(input("What interest rate would you like to use? "))/100
    time = int(input("Over what period of time would you like to be invested (in years)? "))
    principle = float(input("Enter an initial investment amount: "))
    for yearNumber in range(time):
        principle = principle * (1 + rate)
    print (round(principle, 2))
    print("Hello!")
main()
