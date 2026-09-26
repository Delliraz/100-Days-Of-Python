import time
import colorgram
from random import choice
import turtle as turtle_module

MIN_COORD = -500
MAX_COORD = 500
STEP = 50
# COLORS = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "brown", "black", "gray", "cyan", "magenta", "teal", "navy", "maroon", "lime", "olive", "turquoise", "violet"]

COLORS = colorgram.extract("hirst.jpg", 20)
rgb_colors = []
for c in COLORS:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    rgb_colors.append((r, g, b))
print(rgb_colors)


def draw_circle():
    turtle.begin_fill()
    turtle.colormode(255)
    rgb = choice(rgb_colors)
    turtle.color(rgb)
    turtle.circle(10)
    turtle.end_fill()


def go_to_start():
    turtle.goto(-500, -500)


def make_step():
    turtle.forward(STEP)


turtle = turtle_module.Turtle()
turtle.penup()
turtle.speed("fastest")
go_to_start()


while round(turtle.ycor()) <= MAX_COORD:
    while round(turtle.xcor()) <= MAX_COORD:
        draw_circle()
        # turtle.pendown()
        make_step()
    turtle.goto(-500, round(turtle.ycor()) + STEP)


screen = turtle_module.Screen()

screen.screensize(1100, 1100)

screen.exitonclick()
