import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
bg_map = turtle.Turtle()
bg_map.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states=[]
while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's name?").title()

    if answer=="Exit":
        # missing_states=[]
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in state_list if state not in guessed_states]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in state_list:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer]
        # print(state_data.state)
        # print(int(state_data.x),int(state_data.y))
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(state_data.state.item())



# def get_mouse_click_coor(x,y):
#     print(x,y)
# screen.onscreenclick(get_mouse_click_coor)


# screen.mainloop()
