from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#154c79")
screen.title("Welcome to the nostalgic Snake Game!")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.update()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Down", fun=snake.down)

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move_forward()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.position_food()
        scoreboard.ate_food()
        screen.title(f"Snake Game! Current score:{scoreboard.score}")
        snake.extend()

    # Detect collision with wall
    if snake.head.ycor() > 295 or snake.head.xcor() > 295 or snake.head.ycor() < -295 or snake.head.xcor() < -295:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for snake_seg in snake.segments[1:]:
        if snake.head.ycor() == snake_seg.ycor() and snake.head.xcor() == snake_seg.xcor():
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
