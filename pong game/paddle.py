from turtle import Turtle

COLOR = "white"
WIDTH = 5
LENGTH = 1
SHAPE = "square"


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.goto(position)

    def line(self):
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.setheading(270)

        while self.ycor() >= -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def upwards(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def downwards(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




