import turtle
from turtle import Turtle, Screen
import random


# Colors extracted using colorgram.py library (https://pypi.org/project/colorgram.py/) - check colors.py
COLORS = [(237, 230, 96), (13, 115, 170), (166, 79, 46), (188, 12, 63), (213, 157, 87), (129, 181, 203), (234, 76, 46), (33, 139, 83), (5, 34, 91), (146, 167, 35), (76, 40, 21), (110, 187, 165), (167, 47, 91), (227, 117, 147), (14, 170, 212), (59, 160, 89), (6, 95, 51), (219, 71, 119), (95, 21, 69), (240, 162, 190), (147, 205, 224), (12, 87, 106), (211, 222, 10), (248, 170, 145), (9, 45, 127), (7, 75, 41)]
CIRCLE_DIAMETER = 20
NO_OF_CIRCLES_X = 10
NO_OF_CIRCLES_Y = 10
GAP_BETWEEN_CIRCLES = 50

oogway = Turtle()
screen = Screen()

turtle.colormode(255)


def initialize_turtle():
    oogway.speed("fastest")
    oogway.hideturtle()
    oogway.penup()
    oogway.setheading(225)
    oogway.forward(300)
    oogway.setheading(0)


def draw_dots():
    for _ in range(NO_OF_CIRCLES_Y):
        pos_x = oogway.position()[0]
        pos_y = oogway.position()[1]
        for _ in range(NO_OF_CIRCLES_X):
            oogway.dot(CIRCLE_DIAMETER, random.choice(COLORS))
            oogway.forward(GAP_BETWEEN_CIRCLES)
        oogway.setpos(pos_x, pos_y + GAP_BETWEEN_CIRCLES)


initialize_turtle()
draw_dots()
screen.exitonclick()
