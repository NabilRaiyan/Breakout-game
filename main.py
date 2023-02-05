# Importing modules and lib
from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.bgpic('bg.gif')
screen.setup(width=800, height=700)
screen.listen()
screen.tracer(0)
screen.title("Not Breakout")

# Creating objects
paddle = Paddle()
ball = Ball()
bricks = Brick()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()

    # Paddle movement
    screen.onkey(key="Right", fun=paddle.go_right)
    screen.onkey(key="Left", fun=paddle.go_left)

    # Ball movement
    ball.move()

    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Paddle bounce
    if ball.distance(paddle) < 50 and ball.ycor() < -280:
        ball.bounce_y()

    # Collision with the brick
    for brick in bricks.brick_list:
        if ball.distance(brick) < 50:
            bricks.brick_list.remove(brick)
            brick.hideturtle()
            ball.bounce_y()

            # Update scoreboard
            scoreboard.update_score()
            if scoreboard.score > 10 or scoreboard.score > 15 or scoreboard.score > 25:
                ball.ball_speed()

                paddle.paddle_len()

    # Game over
    if ball.ycor() < -330:
        game_is_on = False

    if paddle.length < 2:
        paddle.reset_paddle()
        paddle.paddle_len()

screen.mainloop()
