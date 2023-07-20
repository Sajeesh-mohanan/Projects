from paddle import Paddle
from ball import Ball
from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard

# Setting up screen for ping pong game

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Center line in the screen

ball = Ball()
line = Paddle((0, 350)).line()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
score = Scoreboard()

# paddle movements WS for player 1 and up,down for player 2, calling function from paddle class

screen.listen()
screen.onkeypress(left_paddle.upwards, "w")
screen.onkeypress(left_paddle.downwards, "s")
screen.onkeypress(right_paddle.upwards, "Up")
screen.onkeypress(right_paddle.downwards, "Down")

# while game is on
game_is_on = True
while game_is_on:
    ball.ball_movement()

    # collision with the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y()

    # collision with the paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.ball_bounce_x()

    elif ball.xcor() > 400:
        ball.ball_reset()
        score.l_point()

    elif ball.xcor() < -400:
        ball.ball_reset()
        score.r_point()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
