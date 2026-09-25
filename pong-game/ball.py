from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_collision_with_wall(self):
        if abs(self.ycor()) > 280:
            self.y_move *= -1

    def check_if_catched(self, platform_left, platform_right):
        left_ycor = platform_left.ycor()
        right_ycor = platform_right.ycor()
        if abs(self.xcor()) > 380:
            ball_ycor = abs(self.ycor())
            if self.xcor() < 0 and left_ycor + 60 >= ball_ycor >= left_ycor - 60:
                self.x_move *= -1
                return True
            elif self.xcor() > 0 and right_ycor + 60 >= ball_ycor >= right_ycor - 60:
                self.x_move *= -1
                return True
            print("You lost")
            return False
        return True
