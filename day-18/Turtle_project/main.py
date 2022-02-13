import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########


t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed(0)


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
    print(current_heading)

draw_spirograph(5)

# for _ in range(30):
#      tim.forward(10)
#      tim.penup()
#      tim.forward(10)
#      tim.pendown()

# tim.shape("turtle")
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

screen = t.Screen()
screen = t.Screen()
screen.exitonclick()
