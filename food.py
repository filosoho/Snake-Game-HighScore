from turtle import Turtle
import random

COLOR = ["hot pink", "orange", "turquoise", "deep sky blue", "yellow green", "gold", "medium violet red", "plum",
         "dodger blue", "dark orange", "light sea green", "orange red", "salmon", "pale violet red", "deep pink",
         "dark violet", "slate blue", "olive"]
SHAPE = ["arrow", "turtle", "circle", "square", "triangle", "classic"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(random.choice(SHAPE))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLOR))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.shape(random.choice(SHAPE))
        self.color(random.choice(COLOR))
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
