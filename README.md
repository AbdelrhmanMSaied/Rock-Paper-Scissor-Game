
# Rock-Paper-Scissors Game

An interactive Rock-Paper-Scissors game developed in Python and containerized with Docker. Players compete against the computer by choosing Rock, Paper, or Scissors. The computer randomly selects its move, and the winner is determined according to the game's rules.

## Technologies

- Python 3.13
- Docker

## Features

- Interactive command-line gameplay
- Random computer moves using Python's `random` module
- Input validation for invalid numbers and non-numeric input
- Automatic winner and tie detection
- Option to play multiple rounds
- Docker containerization for a reproducible environment

## Game Rules

- Rock beats Scissors
- Paper beats Rock
- Scissors beats Paper
- Identical choices result in a tie

## Run with Docker

### Build the Docker image

```bash
docker build -t rock-paper-scissors .
```

### Run the game

```bash
docker run -it --rm rock-paper-scissors
```

## Run with Python

If Python 3.13 or another compatible Python 3 version is installed, run:

```bash
python main.py
```

## Concepts Demonstrated

- Variables and data types
- Lists and list indexing
- Loops and conditional statements
- User input and input validation
- Exception handling with `try` and `except`
- Random number generation
- Logical operators
- Functions of a simple interactive game
