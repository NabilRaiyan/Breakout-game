from turtle import Turtle
import random


class Brick:
    def __init__(self):

        self.brick_list = []
        color_list = ['orange', 'cyan']
        for i in range(20):
            brick = Turtle("square")
            brick.penup()

            brick.shapesize(stretch_wid=1, stretch_len=3)
            brick.fillcolor(random.choice(color_list))
            self.brick_list.append(brick)

        for i in self.brick_list:
            i.goto(x=random.randint(-350, 350), y=random.randint(100, 270))



