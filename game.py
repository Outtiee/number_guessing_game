import game_library as gl
import json

# loading user data

with open("userbase.json", "r") as file:
    database = json.load(file)

username = input("Hello. What is your username? ")

for user in database:
    if database["username"] == username:
        print(f"Welcome back {username}")
    else:
        user = gl.User(username)
database[f"{user.username}"] = user.score


# generating a list of possibilities
possibilities = []
for i in range(1):
    possibilities.append(i)
winning_number = gl.target_number(possibilities)
attempts = 1
score = 10_000

# assigning a guess and checking if the guess is correct
while True:
    guess = gl.user_guess()
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

with open("userbase.json", "w+") as file:
    json.dump(database, file)