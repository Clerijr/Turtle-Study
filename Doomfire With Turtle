from turtle import *

# Drawing canvas
screensize(0, 0, "black")
setworldcoordinates(-5, -5, 5, 5)
colormode(255)
ht()

# Created a "pixel" class. They'll change just color and position, in this case, we're using just red
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


# Creating red color tones so they'll got a fading look, the pixels list creates a turtle for each "pixel"
#in the screen, of course it probably have a better way to draw them, but this is a study for turtle right?
red = [255, 235, 215, 195, 175, 155, 135, 115, 95, 75, 50, 30, 10, 0]
pixels = []
y = -4.8
x = -4.9


# The for loop to create the pixels/turtles. Need to improve by adding the random library and use it into the
# flame movement
for p in range(26):
    y = -4.8
    for i in range(13):
        pixels.append(firepixel(red[i], x, y))
        y += 0.5
    x += 0.4




exitonclick()
