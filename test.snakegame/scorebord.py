from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

