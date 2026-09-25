from turtle import Turtle,Screen
from platform import Plattform
from ball import Ball

import scoreboard
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=850,height=650)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

score = Scoreboard()

platform_left = Plattform()
platform_right = Plattform(is_left=False)
ball = Ball()
ball.move()

t = Turtle()
t.penup()
t.goto(-400,-300)
t.pendown()
t.color("white")
t.goto(-400,300)
t.goto(400,300)
t.goto(400,-300)
t.goto(-400,-300)


screen.update()


screen.listen()
screen.onkey(key="w", fun=platform_left.go_up)
screen.onkey(key="s", fun=platform_left.go_down)

screen.onkey(key="Up", fun=platform_right.go_up)
screen.onkey(key="Down", fun=platform_right.go_down)



game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    ball.detect_collision_with_wall()
    time.sleep(0.1)
    if not ball.check_if_catched(platform_left,platform_right):
        game_is_on = False





screen.exitonclick()
