from turtle import Turtle, Screen

# new_turtle = Turtle()
# screen = Screen()
#
# def move_forward():
#     new_turtle.forward(100)
#
# def move_backward():
#     new_turtle.backward(10)
#
# def move_left():
#     current_heading = new_turtle.heading() + 10
#     new_turtle.setheading(current_heading)
#
# def move_right():
#     current_heading = new_turtle.heading() - 10
#     new_turtle.setheading(current_heading)
#
# def clear():
#     new_turtle.clear()
#     new_turtle.penup()
#     new_turtle.home()
#     new_turtle.pendown()
#
#
# screen.listen()
# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=move_backward, key="s")
# screen.onkey(fun=move_left, key="a")
# screen.onkey(fun=move_right, key="d")
# screen.onkey(fun=clear, key="c")

import random
is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
users_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Entre the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [100, 70, 40, 10, -20, -50]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if users_bet:
    is_game_on = True
while is_game_on:
     for turtle in all_turtles:
         if turtle.xcor() > 230:
             is_game_on = False
             winning_color = turtle.pencolor()
             if winning_color == users_bet:
                 print(f"you've won! The {winning_color} turtle is the winner!")
             else:
                 print(f"you've lost! The {winning_color} turtle is the winner!")


         random_dist = random.randint(1, 10)
         turtle.forward(random_dist)


screen.exitonclick()

