import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager=CarManager()
player = Player()
screen.onkeypress(player.move, "Up")


game_is_on = True
while game_is_on:

    for n in range(6):
        time.sleep(0.1)
        screen.update()
        car_manager.move_cars()
        if car_manager.check_crash(player.position()):
            game_is_on=False

    car_manager.create_car()
