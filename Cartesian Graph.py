from turtle import *

'''
Possible changes:
- More smoothness into function drawing
- A input to select a funcion or maybe input a function
'''


def main():
    # Setting the Canvas Size
    setworldcoordinates(-100, -100, 100, 100)
    hideturtle()
    tracer(0)

    # Drawing Lines X and Y
    color("red")
    for i in range(4):
        fd(95)
        bk(95)
        rt(90)

    # Drawing Grid of dots(This draw a spiral)
    speed(1)
    dot(8)
    color('black')
    penup()
    for i in range(1, 87, 2):
        for do in range(i//4):
            pendown()
            dot(6)
            penup()
            fd(10)
        rt(90)
    '''
    # Drawing Grid of dots(simplest way to do it, by using one 'for' for each axis)
    
    color('gray')
    for x in range(-100, 101):
        for y in range(-100, 101):
            if x%5 == 0 and y % 5 == 0: # Best way for scaling the dots into the grid
                pu(); goto(x, y); pd(); dot(4)
    '''

    # Creating Functions
    # Here we can add another funtions based into mathematical equations, easy to add and comprehend

    def function1(x):
        y = x**4 / 4 - x**3 / 3 - 3 * x * x
        return y

    def function2(x):
        y = 1 - 2*x - x**2
        return y

    def function3(x):
        y = x**3 - 6 * x**2 + 4 * x + 12
        return y

    def function4(x):
        y = x**2
        return y

    # Tracing the line
    point = Turtle()
    point.hideturtle()
    point.penup()
    point.color('black')
    point.width(2)
    point.speed(0)

    for x in range(-25, 25):
        y = function4(x) # Select wich function will be used. A input can be used in the future
        point.goto(x*1, y*1) # The current coordinates, can be modified by multiplication for better look into the graphic
        point.pendown()
        print(point.pos()) # This give us a feedback to improve the for cicle and the function drawing

if __name__ == '__main__':
    main()
exitonclick()
