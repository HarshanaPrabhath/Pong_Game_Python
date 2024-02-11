import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle_r = Paddle((380, 0))
paddle_l = Paddle((-380, 0))

ball = Ball()
score = Scoreboard()

screen.onkey(paddle_r.paddle_up, key="Up")
screen.onkey(paddle_r.paddle_down, key="Down")

screen.onkey(paddle_l.paddle_up, key="w")
screen.onkey(paddle_l.paddle_down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # DETECT COLLISION WITH WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECT COLLISION WITH R_PADDLE
    if ball.xcor() > 355 and ball.distance(paddle_r) < 50 or ball.xcor() < -355 and ball.distance(paddle_l) < 50:
        ball.bounce_x()

    # DETECT WHEN BALL IS GOING OUT OF RANGE( r_paddle )
    if ball.xcor() > 370:
        ball.reset_position()
        score.left_score()

    if ball.xcor() < -370:
        ball.reset_position()
        score.right_score()

screen.exitonclick()
