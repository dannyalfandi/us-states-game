import turtle
import pandas

GUESS_COUNT = 50

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# defined coordinate mouse click
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

state_data = pandas.read_csv("50_states.csv")
get_state = state_data["state"].tolist()

answer_list = []

going_game = True
while len(answer_list) < 50:
    answer_state = screen.textinput(title=f"{len(answer_list)} / {GUESS_COUNT} State Correct", prompt="What's another state's name?").title()
    # check_answer = [check for check in get_state if check.lower() == answer_state.lower()]

    if answer_state == "Exit":
        break

    check_answer = state_data[state_data["state"] == answer_state]
    if check_answer.empty:
        print("batsu")
    elif answer_state in answer_list:
        print("Is it done")
    else:
        print("maru")
        answer_list.append(answer_state)
        get_state.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(check_answer.x.item(),check_answer.y.item())
        t.write(check_answer.state.item())

print(get_state)
data_miss_state ={
    "state": get_state
}
data_frame_miss_state = pandas.DataFrame(data_miss_state)

data_frame_miss_state.to_csv("miss_state")

# screen.exitonclick()
