from operator import truediv
from turtle import Turtle,Screen

import scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=650)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()




screen.update()

screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Right", fun=snake.turn_right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score.inc_score()
        snake.increment_tail()
        food.move_to_random()

    if snake.is_dead():
        print("You have lost")
        break




screen.exitonclick()
