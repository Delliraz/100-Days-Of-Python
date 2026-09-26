import time
from random import choice
from turtle import Turtle, Screen


def draw_dash(l):
    count = 0
    while count < l:
        turtle.forward(5)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
        count += 10


turtle = Turtle()

turtle.speed("fastest")


for _ in range(4):
    draw_dash(100)
    turtle.left(90)


screen = Screen()

screen.screensize(1100, 1100)

screen.exitonclick()
