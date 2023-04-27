from turtle import Turtle
import random
P1_POSITION = (-450, 0)
P2_POSITION = (450, 0)

# def __init__(self):
    #     self.plate_parts=[]
    #     self.create_plate()
    # def create_plate(self):
    #     for i in range(4):
    #         new_part=Turtle("square")
    #         new_part.color("white")
    #         new_part.penup()
    #         self.plate_parts.append(new_part)
    #
    # def take_position(self,player):
    #     if player==1:
    #         self.plate_parts[0].goto(P1_POSITION)
    #         self.plate_parts[0].setheading(270)
    #     elif player==2:
    #         self.plate_parts[0].goto(P2_POSITION)
    #         self.plate_parts[0].setheading(270)
    #     print(self.plate_parts[0].position())
    #     y=20
    #     for part in self.plate_parts[1:]:
    #         part.goto(self.plate_parts[0].position())
    #         part.right(90)
    #         part.forward(y)
    #         y+=20
    #
    # def how_many_part(self):
    #     print(len(self.plate_parts))


class Plate(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.penup()

    def take_position(self,player):
        self.goto(P1_POSITION) if player==1 else self.goto(P2_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(30)

    def down(self):
        self.backward(30)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.penup()

    def move(self):
        self.forward(10)

    def determine_angle_r(self):
        angle=random.randint(0,89)
        if angle>45:
            angle+=270
        self.setheading(angle)

    def determine_angle_l(self):
        angle=random.randint(135,225)
        self.setheading(angle)

    def x_position_valid(self):
        if not (-435<self.xcor()<435):
            return False
        else:
            return True

    def y_position_valid(self,ycor):
        if ycor-50<self.ycor()<ycor+50:
            return True
        return False

    def bounce(self):
        if self.heading_to()=="right":
            self.determine_angle_l()
            self.forward(20)
        elif self.heading_to()=="left":
            self.determine_angle_r()
            self.forward(20)

    def heading_to(self):
        if 0<=self.heading()<=45 or 316<=self.heading()<=359:
            return "right"
        elif 135 <= self.heading() <= 225:
            return "left"

    def wall_jump(self):
        if 0<self.heading()<46:
            self.right(self.heading()*2)
        elif 270<self.heading()<360:
            angle=self.heading()%90
            self.left((90-angle)*2)
        elif 180<self.heading()<270:
            angle=self.heading()%90
            self.right(angle*2)
        else:
            angle=self.heading()%90
            self.left((90-angle)*2)