from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.pensize(5)
        self.hideturtle()
    def dashed_line(self, length):
        self.goto(0,-270)
        self.setheading(90)
        for t in range(length//40+1):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
            self.pendown()
            self.forward(10)
