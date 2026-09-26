from operator import truediv
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    seg1_pos = None
    for seg in segments:
        if seg1_pos is None:
            seg1_pos = seg.position()
            seg.forward(20)
        else:
            seg.goto(seg1_pos)


screen.exitonclick()
