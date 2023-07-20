from turtle import Turtle


ALIGNMENT = "center"
FONT = ("COURIER", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read_file())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.display_scoreboard()
        self.hideturtle()

    def display_scoreboard(self):
        self.write(f"Score : {self.score} | High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=("COURIER", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_scoreboard()

    def write_file(self):
        with open("High_Score.txt", mode="w") as file:
            high_score = str(self.high_score)
            file.write(high_score)

    def read_file(self):
        with open("High_Score.txt") as file:
            high_score = int(file.read())
        return high_score


