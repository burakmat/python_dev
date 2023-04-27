from turtle import Turtle


def get_high_score():
    with open("scores.txt") as file:
        return file.read()


def update_high_score(score):
    hscore = int(get_high_score())
    if score > hscore:
        with open("scores.txt", "w") as hs:
            hs.write(str(score))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.pencolor("slate gray")
        self.write(f"Score: 0 High Score: {get_high_score()}", align="center", font=("Arial", 15, "normal"))

    def update_score(self, new_score):
        self.clear()
        self.write(f"Score: {new_score} High Score: {get_high_score()}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 25, "normal"))

