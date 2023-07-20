from turtle import Turtle, Screen
import pandas

trtle = Turtle()
trtle1 = Turtle()
trtle1.penup()
trtle1.hideturtle()
trtle1.speed("fastest")
screen = Screen()
screen.setup(height=500, width=750)
img = "blank_states_img.gif"
csv_data = pandas.read_csv("50_states.csv")
screen.addshape(img)
trtle.shape(img)
right_ans = []


#check weather input answer = value in csv file
states = csv_data["state"].tolist()

while len(right_ans) < 50:
    txt_input = screen.textinput(title="Guess the state", prompt=f"{len(right_ans)}/50 states remaining").title()

    if txt_input == "Exit":

        for rem_state in states:
            if rem_state not in right_ans:
                trtle1.color("red")
                state_data = csv_data[csv_data.state == rem_state]
                trtle1.goto(int(state_data.x), int(state_data.y))
                trtle1.write(rem_state)
        break

    if txt_input in states and txt_input not in right_ans:
        state_data = csv_data[csv_data.state == txt_input]
        trtle1.goto(int(state_data.x), int(state_data.y))
        trtle1.write(txt_input)
        right_ans.append(txt_input)


screen.exitonclick()
