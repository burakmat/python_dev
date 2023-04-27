from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 500)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y = -125
c = 0
finisher = Turtle()
finisher.penup()
finisher.goto(100, -200)
finisher.setheading(90)
finisher.pendown()
finisher.forward(400)
finisher.hideturtle()
for t in range(6):
    name = Turtle("turtle")
    turtles.append(name)
    name.color(colors[c])
    name.penup()
    name.goto(-230, y)
    y += 50
    c += 1


race = True
user_bet = screen.textinput("Make your bet", "Which turtle will win the game?")
while race:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 90:
            print(f"{turtle.pencolor()} win the race!".title())
            if user_bet == turtle.pencolor():
                print("You win.")
            else:
                print("You lose.")
            race = False
            break


screen.exitonclick()
