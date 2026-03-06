import turtle
class Paddles:
    def __init__(self):
        self.paddle1 = turtle.Turtle()
        self.paddle2 = turtle.Turtle()
        self.set_attributes(paddle=self.paddle1, pos=-1)
        self.set_attributes(paddle=self.paddle2, pos=1)
    def set_attributes(self, paddle, pos):
        paddle.shape('square')
        paddle.penup()
        paddle.speed(0)
        paddle.color("white")
        paddle.shapesize(stretch_wid = 4, stretch_len = 1)
        paddle.goto(380*pos, 0)
    def move_paddle(self, paddle, dir):
        x_cord = paddle.xcor()
        y_cord = paddle.ycor()
        if 260 > y_cord > -260:
            paddle.goto(x_cord, y_cord + 10*dir)
        elif y_cord >= 260 and dir == -1:
            paddle.goto(x_cord, y_cord + 10*dir)
        elif y_cord <= -260 and dir == 1:
            paddle.goto(x_cord, y_cord + 10*dir)
    def paddle1_up(self):
        self.move_paddle(self.paddle1, 1)
    def paddle1_down(self):
        self.move_paddle(self.paddle1, -1)
    def paddle2_up(self):
        self.move_paddle(self.paddle2, 1)
    def paddle2_down(self):
        self.move_paddle(self.paddle2, -1)