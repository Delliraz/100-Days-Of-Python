import random
import time
from turtle import Turtle, Screen

COLORS = [
    "red",
    "yellow",
    "blue",
    "green",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "gray",
    "cyan",
    "magenta",
    "teal",
    "navy",
    "maroon",
    "lime",
    "olive",
    "turquoise",
    "violet",
]


turtle = Turtle()

turtle.speed("fastest")
# turtle.pensize(15)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    col = (r, g, b)
    return col


for _ in range(0, 360, 5):
    turtle.rt(_)
    # turtle.color(random_color())
    turtle.circle(100)


screen = Screen()

screen.screensize(1100, 1100)

screen.exitonclick()
