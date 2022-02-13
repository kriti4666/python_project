import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # detect if the turtle cross the road.
    if player.is_at_finished_line():
        player.return_position()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()