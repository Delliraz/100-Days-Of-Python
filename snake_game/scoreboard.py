from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 300)
        self.draw_score()

    def draw_score(self):
        self.write(f"Score: {self.score}", False, "right", font=("Arial", 12, "bold"))

    def inc_score(self):
        self.score += 1
        self.clear()
        self.draw_score()
