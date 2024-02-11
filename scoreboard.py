from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.updated_score()

    def updated_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, font=("arial", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, font=("arial", 40, "normal"))

    def right_score(self):
        self.r_score += 1
        self.updated_score()

    def left_score(self):
        self.l_score += 1
        self.updated_score()

