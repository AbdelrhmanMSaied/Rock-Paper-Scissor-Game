
# Hangman Game

An interactive Hangman Game developed in Python and containerized with Docker. Players try to guess a randomly selected fruit by entering words, with a limited number of attempts before the game ends. The game displays the Hangman stages as incorrect guesses accumulate.

## Technologies

- Python 3.13
- Docker

## Features

- Random word selection
- Fruit-themed word guessing
- Limited attempts
- ASCII Hangman drawings
- Interactive command-line gameplay

## Run with Docker

### Build the Docker image

```bash
docker build -t hangman-game .
```

### Run the game

```bash
docker run -it --rm hangman-game
```

## Concepts Demonstrated

- Python lists and strings
- Loops and conditional statements
- User input and output
- Random word selection using the `random` module
- Basic game logic and attempt tracking
- Docker image building and container execution
