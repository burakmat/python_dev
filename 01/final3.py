Love=[]
Good=[]
World=[]
Money=[]
print("Please enter the words one-by-one, that have meaningful direction or purpose in your life, to find your Ikigai. In order to complete entering for each category, enter Y.")
print("What you love?")
while True:
    love=input()
    if love.lower()!="y":
        Love.append(love)
    else:
        break
print("What you are good at?")
while True:
    good = input()
    if good.lower() != "y":
        Good.append(good)
    else:
        break
print("What the world needs?")
while True:
    world = input()
    if world.lower() != "y":
        World.append(world)
    else:
        break
print("What you can be paid for?")
while True:
    money = input()
    if money.lower() != "y":
        Money.append(money)
    else:
        break
outputDictionary={}

def check():
    Ikigai=set(Love).intersection(Good, World, Money)
    Mission=(set(Love).intersection(World))
    Passion=(set(Love).intersection(Good))
    Profession=(set(Good).intersection(Money))
    Vocation=(set(Money).intersection(World))
    setGood=set(Good)-Profession-Passion
    setLove=set(Love)-Mission-Passion
    setMoney=set(Money)-Profession-Vocation
    setWorld=set(World)-Vocation-Mission
    outputDictionary["Ikigai"]=Ikigai
    outputDictionary["Vocation"]=Vocation
    outputDictionary["Profession"]=Profession
    outputDictionary["Purpose"]=Mission
    outputDictionary["Passion"]=Passion
    outputDictionary["Good"]=setGood
    outputDictionary["Love"]=setLove
    outputDictionary["Money"]=setMoney
    outputDictionary["World"]=setWorld
check()
print(outputDictionary)
