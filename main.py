import turtle
import pandas


screen = turtle.Screen()
screen.setup(width=750, height=550)
screen.title("US STATE GUESSING GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    user_input_state = screen.textinput(title=f"{len(guessed_state)}/50 State",
                                        prompt="What is the next state?").title()

    if user_input_state == "Exit":
        #using list comperhesion method
        missing_names = [state for state in all_states if state not in guessed_state]
        new_file = pandas.DataFrame(missing_names)
        new_file.to_csv("missing_names.csv")
        break
    if user_input_state in all_states:
        guessed_state.append(user_input_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # the condition was checkes inside the csv file,is equal to the user enter name and print the entire row
        new_statement = data[data.state == user_input_state]
        t.goto(int(new_statement.x), int(new_statement.y))
        # item() function return the current value
        t.write(new_statement.state.item())
