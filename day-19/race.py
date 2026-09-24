import turtle
from random import randint
from turtle import Turtle, Screen
import math

COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]

#class MyTurtle(shape,color):
 #   turtle = Turtle()
  #  s



screen = Screen()
chosen_color = turtle.textinput("Make your bet", "Choose your turtle color")
turtles = []

def is_turtle_finished(t):
    return t.xcor() >= 500

def any_turtle_not_finished():
    for t in turtles:
        if t.xcor() < 500:
            return True
    return False

for i in range(5):
    t = Turtle()
    t.penup()
    t.shape("turtle")
    t.color(COLORS[i])
    t.goto(-500,-300 + i*100)
    turtles.append(t)

while any_turtle_not_finished():
    for t in turtles:
        if is_turtle_finished(t):
            print(f"{t.color()} won!")
            break
        distance = randint(5,30)
        t.forward(distance)

screen.exitonclick()
