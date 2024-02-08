import turtle
from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle_r = Paddle((380, 0))
paddle_l = Paddle((-380, 0))

screen.onkey(paddle_r.paddle_up, key="Up")
screen.onkey(paddle_r.paddle_down, key="Down")

screen.onkey(paddle_l.paddle_up, key="w")
screen.onkey(paddle_l.paddle_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
