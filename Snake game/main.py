import time
from snake import Snake
from turtle import Screen
from Food import Food
from ScoreBoard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")


def game_reset():
    screen.clear()
    main()


def main():
    screen.bgcolor("black")
    screen.tracer(0)
    snake_body = Snake()
    food = Food()
    score = Scoreboard()

    screen.onkeypress(snake_body.upward, "Up")
    screen.onkeypress(snake_body.downward, "Down")
    screen.onkeypress(snake_body.left_turn, "Left")
    screen.onkeypress(snake_body.right_turn, "Right")
    screen.listen()

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake_body.move()

        if snake_body.head.distance(food) < 15:
            food.refresh()
            snake_body.extend()
            score.increase_score()

        if snake_body.head.xcor() > 280 or snake_body.head.xcor() < -280 or snake_body.head.ycor() > 280 or snake_body.head.ycor() < -280:
            game_is_on = False
            score.check_high_score()
            score.game_over()
            screen.onkeypress(game_reset, "space")

        for segment in snake_body.segments[1:]:
            if snake_body.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()
                screen.onkeypress(game_reset, "space")


main()
screen.exitonclick()
