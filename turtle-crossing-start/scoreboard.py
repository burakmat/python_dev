from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-285,250)
        self.current_level=1
        self.write(f"Level: {self.current_level}", align="left", font=FONT)

    def level_count(self):
        self.current_level += 1

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="left", font=FONT)

    def end_game(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)