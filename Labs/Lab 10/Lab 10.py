def sumN(n):
    total = 0
    for i in range(0, n+1):
        total += i
    return total
def sumNSquares(n):
    total = 0
    for i in range(0, n+1):
        total += i*i
    return total
def main():
    number = int(input("What number would you like to input? "))
    sumNumber = sumN(number)
    sumSquareNumbers = sumNSquares(number)
    print(sumNumber)
    print(sumSquareNumbers)
main()
