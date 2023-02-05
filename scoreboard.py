from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.score = 0
        self.hideturtle()
        self.color('#FFF2F2')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 280)
        self.write(f"Score: {self.score}", align='center', font=("Courier", 20, 'bold'))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()
