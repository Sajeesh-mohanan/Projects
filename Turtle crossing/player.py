from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE = 200


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.start_point()

    def go_up(self):
        self.forward(10)

    def go_down(self):
        self.back(10)

    def start_point(self):
        self.goto(STARTING_POSITION)

    def finish_point(self):
        if self.ycor() >= FINISH_LINE:
            self.start_point()
            return True
