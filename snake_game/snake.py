from turtle import Turtle
from food import Food

STARTING_POSITIONS = [
    (0, 0),
    (-20, 0),
    (-40, 0),
    (-60, 0),
    (-80, 0),
    (-100, 0),
    (-120, 0),
]
MOVE_DISTANCE = 20


class Snake:
    segments = []
    score = 0

    def __init__(self):
        self.draw_snake()
        self.head = self.segments[0]

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[i - 1].position()
            self.segments[i].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def is_dead(self):
        if abs(self.head.xcor()) >= 300 or abs(self.head.ycor()) >= 300:
            return True
        for tail_part in self.segments[1:]:
            if self.head.position() == tail_part.position():
                return True
        return False

    def draw_snake(self):
        for position in STARTING_POSITIONS:
            self.draw_unit(position)

    def draw_unit(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def turn_up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def turn_left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)

    def turn_down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def increment_tail(self):
        last_unit = self.segments[-1]
        xcor = last_unit.xcor()
        ycor = last_unit.ycor()
        match last_unit.heading():
            case 0:
                xcor -= MOVE_DISTANCE
            case 90:
                ycor -= MOVE_DISTANCE
            case 180:
                xcor += MOVE_DISTANCE
            case 270:
                ycor += MOVE_DISTANCE

        self.draw_unit((xcor, ycor))
