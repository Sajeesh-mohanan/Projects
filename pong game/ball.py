from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = random.choice([15, -15])
        self.y_move = random.randint(-10, 10)

    def ball_reset(self):
        self.goto(0, 0)
        self.y_move = random.randint(-10, 10)
        self.x_move = random.choice([15, -15])
        self.x_move *= -1

    def ball_movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ball_bounce_y(self):
        self.y_move *= -1

    def ball_bounce_x(self):
        self.x_move *= -1 * 1.1



