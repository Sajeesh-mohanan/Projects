from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.show_level()

    def increase_level(self):
        self.clear()
        self.level += 1

    def show_level(self):
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="Center", font=("Caprasimo", 20, "normal"))
