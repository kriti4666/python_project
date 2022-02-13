
from turtle import Turtle, Screen
import random
is_game_on = False
screen = Screen()
screen.setup(width=400, height=400)

user_bet = screen.textinput(title="Make a bet", prompt="Who will win the race? Guess the color: ")
colors = ["red", "orange", "pink", "blue", "green"]
y_position = [-80, -50, -20, 10, 40]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-180, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 180:
            winning_turtle = turtle.pencolor()
            is_game_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won!. the {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost!. the {winning_turtle} turtle is the winner!")


        random_movement = random.randint(0, 10)
        turtle.forward(random_movement)

screen.exitonclick()







