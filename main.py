from turtle import Screen, Turtle

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen_width = 800
screen_height = 600
r_paddle_position = (380, 0)
l_paddle_position = (-380, 0)
screen = Screen()
screen.bgcolor("black")
screen.setup(width=screen_width, height=screen_height)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(r_paddle_position)
l_paddle = Paddle(l_paddle_position)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #Detect collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 340 or ball.distance(l_paddle) < 40 and ball.xcor() < -340:
        ball.bounce_x()
    
    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()  
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()  
        scoreboard.r_point()

screen.exitonclick()