import time
from random import choice
from turtle import Turtle, Screen


turtle = Turtle()

turtle.speed("slow")


for _ in range(3,100):
    count = _
    while count > 0:
        turtle.forward(50)
        turtle.right(360/_)
        count-=1







screen = Screen()

screen.screensize(1100,1100)

screen.exitonclick()

