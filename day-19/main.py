from turtle import Turtle, Screen
tim=Turtle()
screen=Screen()
screen.listen()
def go():
    tim.forward(20)
def back():
    tim.backward(20)
def turn_r():
    tim.right(15)
def turn_l():
    tim.left(15)
def clear():
    tim.reset()
screen.onkey(clear, "c")
screen.onkey(go,"w")
screen.onkey(back,"s")
screen.onkey(turn_r,"d")
screen.onkey(turn_l,"a")
screen.exitonclick()