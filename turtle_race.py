from turtle import Turtle,Screen
import random as r
screen=Screen()
is_race_on=False
screen.setup(width=500,height= 400)
user_bet=screen.textinput(title="Make your Bet", prompt="which turtle will win the race? Enter a color: ").lower()
colors=["red","orange","yellow","green","blue", "purple"]
temp=-100
all_turtles=[]
for i in range(0,len(colors)):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=temp)
    temp+=40
    all_turtles.append(tim)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You,ve won ! The {winning_color} turtle is the winner!!")
                is_race_on = False
            else:
                print(f"You,ve lost ! The {winning_color} turtle is the winner!!")
                is_race_on = False

        random_distance=r.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()