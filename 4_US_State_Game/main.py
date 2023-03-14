import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = turtle.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's game?").title()
    print(answer_state)

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        data_state = data[data.state == answer_state]
        state_turtle.goto(int(data_state.x), int(data_state.y))
        state_turtle.write(answer_state)

#states_to_learn.csv

states_not_founded = [state for state in all_states if state != guessed_states]


df = pandas.DataFrame(states_not_founded)

df.to_csv("states_to_lean")