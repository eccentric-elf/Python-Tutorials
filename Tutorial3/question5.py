import turtle
import math


t = turtle.Turtle()
t.speed(0)


def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.right(60)


for i in range(10):
    angle = i * (360 / 10) 
    t.penup()
    t.goto(math.cos(math.radians(angle)) * 100, math.sin(math.radians(angle)) * 100)
    t.pendown()
    draw_hexagon(50)


turtle.done()
