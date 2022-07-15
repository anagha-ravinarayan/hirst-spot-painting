import turtle
from turtle import Turtle, Screen
import random

oogway = Turtle()
screen = Screen()

turtle.colormode(255)


def random_color_in_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tuple([r, g, b])


# Draw a square
def draw_square():
    for _ in range(4):
        oogway.forward(100)
        oogway.right(90)


# Draw a dashed line
def draw_dashed_line():
    for _ in range(20):
        oogway.forward(10)
        oogway.penup()
        oogway.forward(10)
        oogway.pendown()


# Draw a polygon with 3, 4, 5, 6, 7, 8, 9, 10 sides with one common side, each in a random color
def draw_polygons():
    colors = ["SteelBlue", "Navy", "Firebrick", "Lime", "DarkMagenta", "BlueViolet", "DarkGoldenrod", "DarkGreen", "Chocolate"]
    for sides in range(3, 11):
        angle = 360 / sides
        oogway.pencolor(random.choice(colors))
        for _ in range(sides):
            oogway.forward(100)
            oogway.right(angle)


# Draw a random walk of fixed stride, each with a random color, thicker line and faster drawing
def draw_random_walk():
    directions = [0, 90, 180, 270]
    oogway.pensize(5)
    oogway.speed('fast')
    for _ in range(100):
        oogway.color(random_color_in_rgb())
        oogway.forward(20)
        oogway.setheading(random.choice(directions))


# Draw a spirograph
def draw_spirograph():
    oogway.speed('fastest')
    angle = 5
    no_of_circles = int(360 / angle)
    for _ in range(no_of_circles):
        oogway.color(random_color_in_rgb())
        oogway.circle(100)
        oogway.left(angle)


draw_square()
oogway.clear()
draw_dashed_line()
oogway.clear()
draw_polygons()
oogway.clear()
draw_random_walk()
oogway.clear()
draw_spirograph()
oogway.clear()

screen.exitonclick()
