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
    answer = turtle.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's name? Type Exit to stop.")
    if answer is None or answer.title() == "Exit":
        break
    answer_state = answer.title()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        data_state = data[data.state == answer_state]
        state_turtle.goto(int(data_state.x.item()), int(data_state.y.item()))
        state_turtle.write(answer_state)

# Save the states that were not guessed so they can be practised later
states_to_learn = [state for state in all_states if state not in guessed_states]
pandas.DataFrame(states_to_learn, columns=["state"]).to_csv("states_to_learn.csv", index=False)