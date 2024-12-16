import random
import turtle
import pandas as pd

# Function to generate a random color
def generate_random_color():
    color = []
    for _ in range(3):
        r = random.randint(0, 255)
        color.append(r)
    return tuple(color)

# Load data from CSV file
data_frame = pd.read_csv("50_states.csv")

# Setup Turtle screen
screen = turtle.Screen()
screen.setup(width=725, height=491)

# Image path for the map
IMAGE = "blank_states_img.gif"

# Ensure the image is in .gif format
screen.addshape(IMAGE)

# Create a turtle and set the map as its shape
map_turtle = turtle.Turtle()
map_turtle.shape(IMAGE)

# Enable random colors for turtle drawings
turtle.colormode(255)

# Game variables
is_game_active = True
states_list = data_frame.state.tolist()
guessed_states = []

# Main game loop
while is_game_active and len(guessed_states) < 50:

    # Prompt user to input a state name
    user_guess = turtle.textinput(
        f"Guess State {len(guessed_states)}/{len(data_frame)}",
        "Type the name of a state:"
    ).title()

    # Exit the game and save unguessed states if the user types 'Exit'
    if user_guess == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("missing_states.csv", index=False, header=False)
        is_game_active = False

    # Check if the guessed state is correct
    elif user_guess in states_list and user_guess not in guessed_states:
        guessed_states.append(user_guess)
        state_data = data_frame[data_frame.state == user_guess]
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(state_data.x.item(), state_data.y.item())
        turtle.pendown()
        turtle.write(user_guess, align="center", font=("Arial", 12, "normal"))

# Keep the window open
screen.mainloop()
