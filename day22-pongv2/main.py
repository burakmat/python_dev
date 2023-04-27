from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("red")
screen.setup(1000, 600)
screen.title("Pong")
screen.tracer(0)





r_paddle = Paddle(450)
l_paddle = Paddle(-450)


screen.update()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
while True:
	screen.update()



screen.exitonclick()
