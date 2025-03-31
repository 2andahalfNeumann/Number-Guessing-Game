# Number Guessing Game

Welcome to the **Number Guessing Game**, where you can test your luck and guessing skills! The game presents three difficulty levels, and you must guess a number between 1 and 100 within a limited number of attempts. Along the way, you can receive hints depending on the difficulty level.

## Game Features:

- **Three Difficulty Levels**:
    - **Easy**: 10 chances with 2 hints.
    - **Medium**: 5 chances with 1 hint.
    - **Hard**: 3 chances with no hints.
  
- **Hint System**: Hints are provided at critical points depending on your selected difficulty.

- **Score Tracking**: 
    - Your attempts are saved, including the difficulty, number of attempts, time spent, and whether or not you guessed the correct number.
    - View all scores or top 5 high scores.
    - Scores are stored in a JSON file, and can be paginated for easier navigation.

- **Retry or Exit Options**: After completing a round, you can choose to play again or exit the game.

## Getting Started:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/2andahalfNeumann/Number-Guessing-Game.git
    cd number_guessing_game
    ```

2. **Run the Game**:
    The main game script is `number_game.py`. To start the game, simply run:
    ```bash
    python number_game.py
    ```

3. **Game Options**:
    - Select difficulty: Choose between Easy, Medium, or Hard.
    - View scores: See all previous attempts or view the top 5 highest scores.
    - Exit the game at any time.

4. **Saving and Viewing Scores**:
    - All attempts are saved in the `attempts.json` file.
    - You can view your past attempts and scores by choosing the "View Scores" option during the game.

## Dependencies:

- **Python 3.x**: The game is compatible with Python 3.x versions.
- No additional libraries are required as the game uses standard Python libraries (`random`, `time`, `datetime`, `json`, `os`).

## Enjoy the Game!

Have fun and try to guess the correct number as quickly as possible. Can you make it to the top of the leaderboard? 😎
