from turtle import Turtle,Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def move_left():
    t.left(10)


def move_right():
    t.right(10)

def clear():
    screen.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
