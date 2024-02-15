import colorgram
from turtle import Turtle, Screen
from random import randrange

colors = colorgram.extract('image.jpg', 30)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# print(rgb_colors)

colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
          (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
          (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
          (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
          (176, 192, 208), (168, 99, 102)]

screen = Screen()
screen.colormode(255)

t = Turtle()
t.speed(0)
t.penup()
t.hideturtle()
t.goto(-250, -250)

for i in range(0, 100):
    if i % 10 == 0 and i > 0:
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(500)
        t.right(180)
    t.dot(20, colors[randrange(0, len(colors))])
    t.forward(50)

screen.exitonclick()