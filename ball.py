# import turtle
# class Ball(turtle.Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.color("white")
#         self.penup()
#         self.x_increase = 10
#         self.y_increase = 10
#     def move_ball(self):
#         self.goto(self.xcor()+self.x_increase, self.ycor()+self.y_increase)
#     def bounce_y(self):
#         self.y_increase *= -1
#         print(self.pos())
#     def bounce_x(self):
#         self.x_increase *= -1
#         print(self.pos())
import turtle
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(45)
    def move_ball(self):
        self.forward(10)
    def get_quadrant(self):
        direction = self.heading()
        self.quadrant = None
        if direction < 90:
            self.quadrant = 1
        elif direction < 180:
            self.quadrant = 2
        elif direction < 270:
            self.quadrant = 3
        else:
            self.quadrant = 4
    def bounce_y(self):
        self.get_quadrant()
        top_boundary = 280
        bottom_boundary = -280
        head_increase = (self.heading()+90)%360
        head_decrease =(360+self.heading()-90)%360
        if self.ycor() > top_boundary:
            if self.quadrant == 1:
                self.setheading(head_decrease)
            elif self.quadrant == 2:
                self.setheading(head_increase)
        elif self.ycor() < bottom_boundary:
            if self.quadrant == 3:
                self.setheading(head_decrease)
            elif self.quadrant == 4:
                self.setheading(head_increase)

    def bounce_x(self):
        self.get_quadrant()
        left_boundary = -360
        right_boundary = 360
        head_increase = (self.heading() + 90) % 360
        head_decrease = (360 + self.heading() - 90) % 360
        if self.xcor() > right_boundary:
            if self.quadrant == 1:
                self.setheading(head_increase)
            elif self.quadrant == 4:
                self.setheading(head_decrease)
        elif self.xcor() < left_boundary:
            if self.quadrant == 2:
                self.setheading(head_decrease)
            elif self.quadrant == 3:
                self.setheading(head_increase)
    def reset_ball(self):
        self.goto(0, 0)
        self.setheading(360+(self.heading()*-1+180)%360)