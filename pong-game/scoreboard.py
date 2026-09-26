from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.draw_middleline()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(25, 300)
        self.draw_score()

    def draw_score(self):
        self.write(f"Score: {self.score}", False, "right", font=("Arial", 16, "bold"))

    def inc_score(self):
        self.score += 1
        self.clear()
        self.draw_score()

    def draw_middleline(self):
        self.goto(0, -300)
        self.pendown()
        self.setheading(90)
        self.draw_dash(600)

    def draw_dash(self, l):
        count = 0
        while count < l:
            self.forward(5)
            self.penup()
            self.forward(5)
            self.pendown()
            count += 10
