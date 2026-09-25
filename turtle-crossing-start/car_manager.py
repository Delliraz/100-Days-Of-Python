from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars = []


class CarManager:
    speed = STARTING_MOVE_DISTANCE

    def __init__(self):
        pass

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance != 1:
            return
        t = Turtle()
        t.shape("square")
        t.penup()

        t.shapesize(stretch_len=2, stretch_wid=1)
        t.color(random.choice(COLORS))
        t.goto(370, random.randint(-250, 250))
        t.seth(180)
        cars.append(t)

    def make_step(self):
        for car in cars:
            car.forward(self.speed)

    def detect_collision(self, player) -> bool:
        for car in cars:
            if car.distance(player) < 20:
                print("Collision")
                return True
        return False

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
