from turtle import Turtle
import random
import turtle


class Car(Turtle):

    def __init__(self, number):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        turtle.colormode(255)
        self.color(self.car_color())
        self.goto(x=random.randint(300, 800), y=180-(number*45))
        self.setheading(180)
        self.car_movement(5)

    def car_movement(self, car_speed):
        self.forward(car_speed)

    def car_color(self):
        r = random.randint(0, 230)
        g = random.randint(0, 230)
        b = random.randint(0, 230)
        color_tup = (r, g, b)
        return color_tup

