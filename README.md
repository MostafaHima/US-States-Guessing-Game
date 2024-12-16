# US States Guessing Game

## Overview
This is an interactive Python game where players guess the names of U.S. states. The game uses Turtle graphics to display a map of the U.S., and the player’s task is to correctly identify all 50 states by typing their names. If the player decides to exit the game, the unguessed states are saved to a CSV file for later reference.

## How It Works
1. The program displays a blank map of the U.S. using Turtle graphics.
2. Players are prompted to type the name of a state.
3. Correct guesses are displayed on the map at the corresponding state’s location.
4. If the player types "Exit," the game ends, and the states they missed are saved to a file named `missing_states.csv`.

## Features
- Interactive map using Turtle graphics.
- Dynamic prompts to track the player’s progress.
- Saves missed states to a CSV file for further learning.
- Random color generation functionality (not directly used in this version).

## Requirements
- Python 3.6 or higher
- Required libraries:
  - `turtle`
  - `pandas`
  - `random`

## Installation
1. Clone this repository or download the source code.
2. Ensure you have Python installed on your system.
3. Install the required libraries:
   ```bash
   pip install pandas
   ```
4. Place the `50_states.csv` file and the `blank_states_img.gif` map image in the same directory as the Python script.

## How to Play
1. Run the script:
   ```bash
   python us_states_game.py
   ```
2. A map of the U.S. will appear.
3. Enter the name of a state in the prompt. If correct, the state name will appear on the map.
4. To end the game early, type "Exit." A file named `missing_states.csv` will be created, listing the states you didn’t guess.

## File Structure
- `main.py`: Main script.
- `50_states.csv`: Contains the names and coordinates of all 50 states.
- `blank_states_img.gif`: Background map image.
- `missing_states.csv`: Generated during gameplay, containing unguessed states.

## Example Output
- After guessing correctly:
  - The guessed state name appears on the map at its correct location.
- Upon exiting:
  - A file `missing_states.csv` is created with the following format:
    ```csv
    Texas
    California
    Florida
    ...
    ```
