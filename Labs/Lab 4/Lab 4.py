def questions():
    #ask questions and make answers global variables
    global name
    name = input("What is your name? ")
    global favNumber
    favNumber = input("What is your favorite number? ")
    global weather
    weather = input("What is the temperature today? ")
    
def nameMultiplied():
    #asking consent
    nameRepeatResponse = input("Would you like to see your name said as many times in a row as your favorite number? (y/n)? ")
    #testing if consent given
    if nameRepeatResponse == "y":
        print("Okay!")
        print(name * int(favNumber))
    else:
        if nameRepeatResponse == "n":
            print("Okay...")
        else:
        #if answer doesn't fall under parameters, re-asking
            nameMultiplied()
            
def main():
    #judging weather
    if int(weather) >= 85:
        judgedWeather = "warm"
    else:
        if int(weather) <= 65:
            judgedWeather = "chilly"
        else:
            judgedWeather = "nice"
    #compile first sentence
    print("Hello, " + name + "! It sure is " + judgedWeather + " out today! ")
    #call nameMultiplied
    nameMultiplied()
    
questions()
main()
