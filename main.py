#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import logo
import random

# Function to reduce player Life
def lifeReduction (life):
  return life - 1

# Function to compare the player guess (playerInput) with the random guessed number (computerGuess)
def compare(playerInput, computerGuess):
  if playerInput > computerGuess:
    return print("Too High.")
  elif playerInput < computerGuess:
    return print("Too Low.")

# Function to check the difficult of the game and return the amount of lives to play
def checkingDifficulty (difficultLevel):
  if difficultLevel == 'easy':
    return 10
  elif difficultLevel == 'hard':
    return 5

print(logo.logo)
print("Welcome to the Number Guessing Game")


def mainGame ():
  print("I am guessing a number between 1 and 100")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  numberGuess = random.randint(1, 100)

  gameMode = True
  playerLife = checkingDifficulty(difficulty)
  while gameMode == True:
    print(f"You have {playerLife} attempts remaining to guess the number")
    playerGuess = int(input("Make a guess: "))
    if playerGuess != numberGuess:
      compare(playerGuess, numberGuess)
      playerLife -= 1
      if playerLife == 0:
        print(f"Game Over, You were unable to guess the number, the number was {numberGuess}")
        gameMode = False
      else:
        print("Guess Again.")
    elif playerGuess == numberGuess:
      print(f"You have {playerLife} attempts remaining to guess the number")
      print(f"You are correct, the number is {numberGuess}")
      gameMode = False

mainGame()


