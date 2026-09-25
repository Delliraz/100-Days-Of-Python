from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(0)

    def move(self):
        self.forward(20)

    def detect_collision_with_wall(self):
        print(self.ycor())
        if abs(self.ycor()) > 300:
            current_heading = self.heading()
            self.setheading(current_heading + 90)


    def check_if_catched(self, platform_left, platform_right):
        left_ycor = platform_left.ycor()
        right_ycor = platform_right.ycor()
        if  abs(self.xcor()) > 390:
            ball_ycor = abs(self.ycor())
            if self.xcor() < 0 and left_ycor +60 >= ball_ycor >= left_ycor -60:
                self.setheading(0)
                return True
            elif self.xcor() > 0 and right_ycor +60 >= ball_ycor >= right_ycor-60:
                self.setheading(180)
                return True
            print("You lost")
            return False
        return True

