
import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)


data = pandas.read_csv("50_states.csv")

states = data["state"]
states_list = states.tolist()
guessed_list = []
# missed_list = []

# x_coordinate_list = data["x"].tolist()
# y_coordinate_list = data["y"].tolist()
while len(guessed_list) < 50:
    answer = turtle.textinput(title=f"{len(guessed_list)}/50 States Correct.", prompt="Guess another states name?").title()
    if answer == "Exit":
        break

    for state in states_list:
        if state == answer:
            writing_turtle = turtle.Turtle()
            writing_turtle.hideturtle()
            writing_turtle.penup()
            state_data_row = data[data.state == answer]
            writing_turtle.goto(int(state_data_row.x), int(state_data_row.y))
            writing_turtle.write(arg=state, align="left")
            guessed_list.append(state)



missing_list = [state for state in states_list if state not in guessed_list]


new_list = pandas.DataFrame(missing_list)
new_list.to_csv("Missed_states")