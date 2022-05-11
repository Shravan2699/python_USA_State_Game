import turtle

import pandas
data = pandas.read_csv("50_states.csv")

from turtle import Turtle,Screen


tim = Turtle()
screen = Screen()
jim = Turtle()

img = "C:/Users/abc/Desktop/Angela Yu Course/Day-25/US game/blank_states_img.gif"
screen.addshape(img)
tim.shape(img)
turtle.title("U.S.States Game")
screen.setup(width=800,height=600,)


state_names = data.state
data_dict = data.to_dict()
data['new_col'] = list(zip(data.x,data.y))
location = data['new_col'].tolist()
ycords = data['y'].tolist()
xcords = data['x'].tolist()
names = data['state'].tolist()
names1 = names
lower_names = []
for i in names:
    new_name = i.lower()
    lower_names.append(new_name)
# print(lower_names)
score = 0
correct_answers = []
remaining_correct_answers = []
game_over = False

while game_over is False:
    answer = screen.textinput(title=f"{score}/50 States Correct",prompt="What's another state's name?").lower()
    if answer == "exit":
        remaining_correct_answers = [ele for ele in names1 if ele not in correct_answers]
        game_over = True


    for i in lower_names:
        if answer == i:
            loc = lower_names.index(answer)
            jim.penup()
            jim.goto(xcords[loc],ycords[loc])
            jim.write(names[loc])
            jim.hideturtle()
            correct_answers.append(names[loc])
            score+=1
            if score == 50:
                print("You win")
                game_over = True


print(remaining_correct_answers)
print(len(remaining_correct_answers))
df = pandas.DataFrame(remaining_correct_answers, columns=["Remaining States"])
df.to_csv('states_to_learn.csv', index=True)
