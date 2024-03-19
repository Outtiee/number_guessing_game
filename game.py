import game_library as gl
import json

username = input("Hello. What is your username? ")

# generating a list of possibilities
possibilities = []
for i in range(1):
    possibilities.append(i)
winning_number = gl.target_number(possibilities)
attempts = 1
score = 10_000

# prompting a guess, checking if it is correct and altering the score accordingly
while True:
    guess = input("I'm guessing you're thinking about the number ")
    active = gl.check_results(guess, winning_number)
    if active == False:
        break
    elif active != "error":
        attempts += 1
        score -= 100
    else:
        continue



print(f"\n\tNumber of attempts: {attempts}"
      f"\n\t Your score: {score}")