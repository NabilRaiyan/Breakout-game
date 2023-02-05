from turtle import Turtle




class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.move_x = 10
        self.move_y = 10
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(x=new_x, y=new_y)

    def bounce_x(self):
        self.move_x *= -1

    def bounce_y(self):
        self.move_y *= -1

    def ball_speed(self):
        self.speed *= 0.9
