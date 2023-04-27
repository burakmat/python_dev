from turtle import Turtle


class Snake:
	def __init__(self):
		self.segments = []

	def create_snake(self):
		for a in range(3):
			new_seg = Turtle("square")
			new_seg.color("white")
			new_seg.penup()
			new_seg.goto(len(self.segments) * -20, 0)
			self.segments.append(new_seg)

	def move(self):
		for i in range(len(self.segments) - 1, 0, -1):
			newx = self.segments[i - 1].xcor()
			newy = self.segments[i - 1].ycor()
			self.segments[i].goto(newx, newy)
		self.segments[0].forward(20)

	def up(self):
		if self.segments[0].heading() != 270:
			self.segments[0].setheading(90)

	def down(self):
		if self.segments[0].heading() != 90:
			self.segments[0].setheading(270)

	def right(self):
		if self.segments[0].heading() != 180:
			self.segments[0].setheading(0)

	def left(self):
		if self.segments[0].heading() != 0:
			self.segments[0].setheading(180)