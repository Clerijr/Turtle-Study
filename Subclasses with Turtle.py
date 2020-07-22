from turtle import *

setworldcoordinates(-50, -50, 50, 50)

# Let's create a standard turtle, a virtual green tortoise, it will not show into screen until we call with another subclass
class tortoise(Turtle):
        def __init__(self, color="green"):# Here we input the "changeable" attributes
                Turtle.__init__(self, shape="turtle") # Here we initiate the Turtle Object
                self.color(color)
                self.shapesize(3)
                self.penup()
                self.ht()
                self.goto(-50, 0)
# Now we created an flying tortoise, we can't see it without calling her,
# So, let's create a racing tortoise! It'll be our normal tortoise but with another attributes
class racingtortoise(tortoise):
        def __init__(self):
                tortoise.__init__(self)
                self.st()
                self.speed(4) #That's a speedy boi
                while self.xcor() <= 45:
                        self.forward(2)
                        print(self.position())

# Now we need some finish line right?
fline = Turtle()

fline.speed(0); fline.ht(); fline.penup(); fline.goto(45, 45)
fline.pendown(); fline.pencolor("red"); fline.width(2); fline.setheading(270); fline.forward(90)

x = racingtortoise()
#This only variable is enough to make our first tortoise, then racing tortoise, run to the finish line

exitonclick()