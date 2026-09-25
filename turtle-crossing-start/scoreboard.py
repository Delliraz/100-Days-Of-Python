from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    level = 1
    text = "Current level"

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-380, 250)
        self.draw_score()

    def draw_score(self):
        self.write(f"{self.text}: {self.level}", False, "left", font=FONT)

    def increment_level(self):
        self.level += 1

    def finish_game(self):
        self.text = "GAME OVER"
        self.goto(-200, 0)
        self.draw_score()
