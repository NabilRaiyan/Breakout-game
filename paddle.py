from turtle import Turtle



class Paddle(Turtle):
    def __init__(self):
        super().__init__('square')
        self.color('white')
        self.length = 5

        self.penup()
        self.goto(x=0, y=-300)
        self.move_right = 30
        self.move_left = -30
        self.update_paddle_len(width=1)

    def update_paddle_len(self, width):
        self.shapesize(stretch_wid=width, stretch_len=self.length)

    def go_right(self):
        new_x = self.xcor() + self.move_right
        self.goto(x=new_x, y=self.ycor())

    def go_left(self):
        new_x = self.xcor() + self.move_left
        self.goto(x=new_x, y=self.ycor())

    def paddle_len(self):
        self.length -= 1
        print(self.length)
        if self.length == 0:
            self.length = 2
        self.update_paddle_len(width=1)

    def reset_paddle(self):
        self.length = 5
        self.update_paddle_len(width=1)
