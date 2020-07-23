from turtle import *
from random import *

screensize(0, 0, "black")
setworldcoordinates(-5, -5, 5, 5)
colormode(255)
ht()

class firepixel(Turtle):
    def __init__(self, red, x, y):
        super().__init__()
        self.ht()
        self.penup()
        self.speed(10)
        self.shape("square")
        self.color(red, 0, 0)
        self.shapesize(2)
        self.goto(x, y)
        self.st()


red = [255, 235, 215, 195, 175, 155, 135, 115, 95, 75, 50, 30, 10, 0]
pixels = []
y = -4.8
x = -4.9

for p in range(26):
    y = -4.8
    for i in range(13):
        pixels.append(firepixel(red[i], x, y))
        y += 0.5
    x += 0.4

exitonclick()