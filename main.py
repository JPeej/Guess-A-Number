import random
import art
import os

def reduce_attempts():
    return attempts - 1

print(art.logo)
print("Welcome to the guess a number game.")

answer = random.randint(1,100)

print("I am thinking of a number between: 1 and 100.")

difficulty = input("Would you like to play the easy game or hard game? Type 'easy' or 'hard': ").strip().lower()

if difficulty == 'easy':
    attempts  = 10
else:
    attempts = 5

print(f"You start with {attempts} attempts on {difficulty} difficulty.")

while attempts > 0:
    guess = int(input("Make a guess: ").strip())

    if guess > answer:
        print("Too high. Guess again")
        attempts = reduce_attempts()

    elif guess < answer:
        print("Too low. Guess again.")
        attempts = reduce_attempts()

    else:
        print(f"You guessed correctly, the answer was {answer}.")
        break

    print(f"You have {attempts} attempts remaining to guess the number.")

