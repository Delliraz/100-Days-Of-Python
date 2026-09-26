from random import randint
from traceback import format_list
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.move_to_random()

    def move_to_random(self):
        self.goto(self.generate_random_position())

    def generate_random_position(self):
        xcord = random.randint(-299, 299)
        ycord = random.randint(-299, 299)
        return (xcord, ycord)
