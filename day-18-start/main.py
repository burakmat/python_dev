from turtle import Turtle, Screen
from random import random,choice
import colorgram
tim = Turtle()
screen = Screen()
tim.hideturtle()
tim.shape("classic")
tim.speed("fastest")


# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# for i in range(10):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()


def change_color():
    R = random()
    G = random()
    B = random()
    tim.color(R,G,B)
# tim.pensize(1)
# for number_of_edge in range(3,11):
#     change_color()
#     for i in range(number_of_edge):
#         tim.forward(100)
#         tim.right(360/number_of_edge)


# for n in range(int(18)):
#     change_color()
#     tim.circle(50)
#     tim.right(20)

colors=colorgram.extract("image.jpg",30)
rgb_colors=[]

for color in colors:
    r= color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(type(colors[0]))





# color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
# screen.colormode(255)
# tim.penup()
# tim.right(90)
# tim.forward(300)
# tim.right(90)
# tim.forward(300)
# tim.right(180)
#
# for n in range(10):
#     for m in range(10):
#         current_color = choice(color_list)
#         tim.color(current_color)
#         tim.dot(20)
#         tim.forward(50)
#     tim.backward(500)
#     tim.left(90)
#     tim.forward(50)
#     tim.right(90)








# def go_right():
#     tim.right(90)
#     tim.forward(20)
# def go_left():
#     tim.left(90)
#     tim.forward(20)
# def go_straight():
#     tim.forward(20)
# def go_back():
#     tim.back(20)
# tim.speed(0)
# tim.pensize(5)
# for i in range(100):
#     change_color()
#     a=choice([go_back,go_left,go_right, go_straight])
#     a()
screen.exitonclick()
