import random
def numGen():
    outfile=open("numbersWrite.txt","w")
    for j in range(20):
        for i in range (10):
            x=random.randint(1,100)
            if len(str(x))==2:
                print(x,end=" ",file=outfile)
            else:
                print(x,end=" ",file=outfile)
        print("",file=outfile)
    outfile.close()

def numAvg():
    infile=open("numbersWrite.txt", "r")
    numbers = infile.read()
    numList = numbers.split()
    length = len(numList)
    trackingVal = 0
    for i in range(0, length):
        trackingVal += int(numList[i])
    avgVal = trackingVal / length
    print(avgVal)

def main():
    numGen()
    numAvg()
main()
