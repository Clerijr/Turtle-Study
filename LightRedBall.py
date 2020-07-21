from turtle import *

def main():
    # Setting the canvas size and sending the turtle to the position
    setworldcoordinates(-250, -250, 250, 250)
    getscreen()
    tracer(0); ht(); pu(); setpos(-180, 180); pd()

    # Setting variables

    radius = 250
    rt(135)
    colormode(255)
    red = 255
    green = 0
    blue = 0

    # Doing the circles
    for i in range(85): # More for cicles, more smoothness in the image
        color(red, green, blue)
        begin_fill()
        circle(radius)
        end_fill()
        radius -= 3
        green = green + 3 # The range number is correlated with the colors increment by the relation range*color increment = 255,
        blue = blue + 3   # that's the simplest way to avoid the program to get a color value bigger than 255 and return a error

    pu();rt(90);forward(5);lt(90);pd(); # That's the final part, i want to draw a circle, or a couple of them, to make
    begin_fill();circle(4);end_fill() # the figure more organic. Without it, you can see a bright red line in the end.

if __name__ == '__main__':
    main()

exitonclick()
