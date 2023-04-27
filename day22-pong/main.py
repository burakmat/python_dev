from turtle import Screen
from scoreboard import Scoreboard
from player_plate import Plate, Ball
import time
screen=Screen()
screen.setup(1000,600)
screen.title("Pong")
screen.tracer(0)
screen.bgcolor("red")
scoreboard=Scoreboard()
scoreboard.dashed_line(540)
plate1=Plate()
plate1.take_position(1)
plate2=Plate()
plate2.take_position(2)
ball=Ball()
screen.update()
time.sleep(3)
screen.listen()
screen.onkeypress(plate2.up, "Up")
screen.onkeypress(plate2.down, "Down")
screen.onkeypress(plate1.up, "w")
screen.onkeypress(plate1.down, "s")
ball.determine_angle_r()
while 1:
    screen.update()
    while ball.x_position_valid():
        ball.move()
        screen.update()
        time.sleep(0.02)
        if ball.ycor()>280 or ball.ycor()<-280:
            ball.wall_jump()
    if ball.y_position_valid(plate1.ycor() if ball.heading_to()=="left" else plate2.ycor()):
        ball.bounce()
        screen.update()
        time.sleep(0.02)
        while not ball.x_position_valid():
            ball.move()
    else:
        break
print("Game Over")
screen.exitonclick()