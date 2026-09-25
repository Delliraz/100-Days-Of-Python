import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
car_manager.add_car()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
count = 6
while game_is_on:
    time.sleep(0.1)
    if car_manager.detect_collision(player):
        scoreboard.finish_game()
        # game_is_on = False
    else:
        car_manager.make_step()
        if player.level_finished():
            scoreboard.increment_level()
            car_manager.increase_speed()

        car_manager.add_car()

    screen.update()
