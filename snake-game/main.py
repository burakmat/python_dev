from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard, update_high_score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("light salmon")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
food.place()
scoreboard = Scoreboard()
screen.update()
time.sleep(3)
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
end_game = False
while not end_game:
    snake.move_snake()
    if snake.parts[0].distance(food) < 15:
        food.place()
        scoreboard.update_score(food.what_score_is())
        snake.add_part()
    screen.update()
    time.sleep(0.1)
    if snake.parts[0].xcor() < -280 or snake.parts[0].xcor() > 280 or \
            snake.parts[0].ycor() < -280 or snake.parts[0].xcor() > 280:
        scoreboard.game_over()
        break
    for part in snake.parts[1:]:
        if snake.parts[0].distance(part) < 10:
            scoreboard.game_over()
            end_game = True
update_high_score(food.what_score_is() - 1)

screen.exitonclick()
