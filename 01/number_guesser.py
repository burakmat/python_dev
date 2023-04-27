import random
maxNumber=int(input("Enter your range: "))
result=str
minNumber=1
while result != "c":
    guess=random.randint(minNumber,maxNumber)
    if minNumber == maxNumber:
        break
    print(f"{guess} is your number?")
    #print(minNumber,maxNumber)
    result=input()
    if result == "h":
        maxNumber=guess-1
    elif result == "l":
        minNumber=guess+1

print(f"The number was {guess}, thanks for playing!")