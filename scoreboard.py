FONT = ("Courier", 50, "normal")
ALIGNMENT = "center"
import turtle
class Scoreboard:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        self.writer = turtle.Turtle()
        self.l_score_disp = turtle.Turtle()
        self.r_score_disp = turtle.Turtle()
        self.draw_border()
        self.setup_score(self.l_score_disp, -1)
        self.setup_score(self.r_score_disp, 1)
    def draw_border(self):
        self.writer.hideturtle()
        self.writer.pencolor("white")
        self.writer.penup()
        self.writer.goto(0, 300)
        self.writer.setheading(270)
        self.writer.pensize(5)
        for x in range(30):
            self.writer.pendown()
            self.writer.forward(10)
            self.writer.penup()
            self.writer.forward(10)
    def setup_score(self, disp, direction):
        disp.hideturtle()
        disp.pencolor("white")
        disp.penup()
        disp.goto(direction * 40, 250)
        disp.write(arg=0, align=ALIGNMENT, font=FONT)
    def update_l_score(self):
        self.l_score_disp.clear()
        self.left_score += 1
        self.l_score_disp.write(arg= self.left_score, align=ALIGNMENT, font=FONT)
    def update_r_score(self):
        self.r_score_disp.clear()
        self.right_score += 1
        self.r_score_disp.write(arg= self.right_score, align=ALIGNMENT, font=FONT)
