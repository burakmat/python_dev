from turtle import Turtle


class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()

    def create_snake(self):
        x = 0
        for i in range(3):
            new_part = Turtle("square")
            new_part.color("lavender")
            new_part.penup()
            new_part.setposition(x, 0)
            self.parts.append(new_part)
            x -= 20

    def move_snake(self):
        for part in range(len(self.parts) - 1, 0, -1):
            newx = self.parts[part - 1].xcor()
            newy = self.parts[part - 1].ycor()
            self.parts[part].goto(newx, newy)
        self.parts[0].forward(20)

    def add_part(self):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        self.parts.append(new_part)
        self.parts[-1].goto(self.parts[-2].xcor(),self.parts[-2].ycor())

    def up(self):
        if self.parts[0].heading() != 270 and self.parts[0].heading() != 90:
            self.parts[0].setheading(90)
            # self.parts[0].forward(20)

    def down(self):
        if self.parts[0].heading() != 90 and self.parts[0].heading() != 270:
            self.parts[0].setheading(270)
            # self.parts[0].forward(20)

    def right(self):
        if self.parts[0].heading() != 180 and self.parts[0].heading() != 0:
            self.parts[0].setheading(0)
            # self.parts[0].forward(20)

    def left(self):
        if self.parts[0].heading() != 0 and self.parts[0].heading() != 180:
            self.parts[0].setheading(180)
            # self.parts[0].forward(20)
