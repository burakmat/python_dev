from random import choice, randint
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars=[]

    def create_car(self):
        new_car=Turtle()
        new_car.shape("square")
        new_car.color(choice(COLORS))
        new_car.shapesize(stretch_len=2)
        new_car.penup()
        new_car.setheading(180)
        ycor = randint(-250, 250)
        new_car.goto(320, ycor)
        self.cars.append(new_car)

    def move_cars(self,level__):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE+self.speed_up_cars(level__))

    def check_crash(self, turtle_cor):
        for car in self.cars:
            if car.distance(turtle_cor)<30  and car.ycor()-25<turtle_cor[1]<car.ycor()+17:
                return True
        return False

    def speed_up_cars(self, level):
        return (level-1)*MOVE_INCREMENT
