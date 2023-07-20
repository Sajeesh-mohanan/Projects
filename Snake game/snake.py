from turtle import Turtle

MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_tail((-20 * i, 0))

    def add_tail(self, position):
        tail = Turtle(shape="circle")
        tail.color("white")
        tail.penup()
        tail.setpos(position)
        self.segments.append(tail)

    def extend(self):
        self.add_tail(self.segments[-1].position())

    def move(self):

        snake_tails = self.segments
        for snake_tail in range(len(snake_tails) - 1, 0, -1):
            new_x = snake_tails[snake_tail - 1].xcor()
            new_y = snake_tails[snake_tail - 1].ycor()
            snake_tails[snake_tail].goto(new_x, new_y)

        snake_tails[0].forward(MOVING_DISTANCE)

    def upward(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def downward(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left_turn(self):

        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right_turn(self):

        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
        


