import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.speed(0)
color_list = [(132, 205, 205), (221, 106, 106), (32, 61, 61), (199, 148, 148), (166, 48, 48), (141, 162, 162), (39, 157, 157), (237, 90, 90), (150, 66, 66), (216, 71, 71), (168, 33, 33), (235, 157, 157), (51, 90, 90), (35, 55, 55), (156, 31, 31), (17, 71, 71), (52, 49, 49), (230, 166, 166), (170, 221, 221), (57, 48, 48), (184, 113, 113), (32, 109, 109), (105, 159, 159), (175, 188, 188), (34, 210, 210), (65, 56, 56)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

