from turtle import  Screen
import time
from player import Player
from CarObjects import Car
from level import Level


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
level = Level()

# initializing Turtle player

player = Player()
cars = []
car_speed = 5


def car_objects():

    for i in range(0, 9):
        new_car = Car(i)
        cars.insert(i, new_car)


screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")


game_over = False
wave = 20
car_objects()


while not game_over:
    level.show_level()
    if wave >= 20:
        car_objects()
        wave = 0
    for car in cars:
        car.car_movement(car_speed)

        if car.distance(player) < 30:
            level.game_over()
            game_over = True

    if player.finish_point():
        level.increase_level()
        car_speed += 2

    screen.update()
    time.sleep(0.1)
    wave += 1

screen.exitonclick()
