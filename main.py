import turtle
import paddles
import ball
import time
import scoreboard
screen = turtle.Screen()
screen.bgcolor("black")
screen.listen()
screen.setup(width=800, height=600)
screen.title("Pong")
turtle.tracer(0)

ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()
paddles = paddles.Paddles()
def end_game():
    global game_on
    game_on = False
screen.onkeypress(key="w", fun=paddles.paddle1_up)
screen.onkeypress(key="s", fun=paddles.paddle1_down)
screen.onkeypress(key= "Up", fun= paddles.paddle2_up)
screen.onkeypress(key= "Down", fun= paddles.paddle2_down)
screen.onkey(key= "space", fun= end_game)
game_on = True
time_delay = 0.1
while game_on:
    turtle.update()
    time.sleep(time_delay)
    if ball.xcor() > 355 or ball.xcor() < -355:
        if ball.distance(paddles.paddle1) < 50 or ball.distance(paddles.paddle2) < 50:
            ball.bounce_x()
            time_delay *= 0.7
        if ball.xcor() > 380:
            # end_game()
            scoreboard.update_l_score()
            time_delay = 0.1
            ball.reset_ball()
        if ball.xcor() < -380:
            scoreboard.update_r_score()
            time_delay = 0.1
            ball.reset_ball()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    ball.move_ball()
screen.exitonclick()