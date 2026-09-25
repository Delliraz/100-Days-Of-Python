from turtle import Turtle

class Plattform(Turtle):

    def __init__(self, is_left:bool = True):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=6)
        self.penup()
        self.color("white")
        if is_left:
            self.goto(-400,0)
        else:
            self.goto(400,0)

    def go_up(self):
        if self.ycor() < 250:
            self.forward(30)

    def go_down(self):
        if self.ycor() > -250:
            self.backward(30)