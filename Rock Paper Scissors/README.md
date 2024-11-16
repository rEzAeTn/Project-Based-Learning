# Rock-Paper-Scissors-Game

## Description
Rock, Paper, Scissors is a command-line Python game where players can compete against the computer or another player. The game supports multiple rounds, displays real-time scores, and allows players to quit at any time by entering Q.

## Features
- **Game Modes:**
    - Player vs Computer
    - Player vs Player
- **Quit Anytime:** Players can quit by entering Q during any prompt.
- **Score Tracking:** Scores are displayed at the beginning of each round.
- **Winner Announcement:** Personalized winner announcements for each round and overall game.

## Directory Structure
```
rock-paper-scissors/
|-- src/
| |-- rock_paper_scissors.py   # Main game logic
|-- README.md                  # Documentation
```

## How To Run
- Clone the repository to your local system.
```bash
git clone https://github.com/rEzAeTn/Project-Based-Learning.git/Rock Paper Scissors
cd rock-paper-scissors
```
- Open your command line and navigate to the main project directory.
- Run `pip install -r requirements.txt` to install necessary dependencies.
- Add the current directory to the `PYTHONPATH` and run the `main.py` script:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```
- Run `python rock_paper_scissors.py` to start the game.
- Follow the on-screen prompts to play the game.
    - Choose the game mode (Player vs Computer or Player vs Player).
    - Enter your name(s) and the number of rounds.
    - Select your choices in each round (Rock, Paper, or Scissors).
    - Quit anytime by entering Q.