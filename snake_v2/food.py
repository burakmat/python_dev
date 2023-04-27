from turtle import Turtle
import random

class Food(Turtle):
	def __init__(self):
		super().__init__("circle")
		self.shapesize(0.5, 0.5)
		self.penup()
		self.color("blue")
		self.speed("fastest")
		self.goto(random.randint(-280, 280), random.randint(-280, 280))




def A():
	B()


def B():
	print("askdla")

A()