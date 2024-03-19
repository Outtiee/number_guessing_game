import game_library as gl
import json

username = input("Hello. What is your username? ")

user_list = [{"username": "admin", "score": 0}]

# need to create read-write json to store user data


for user in user_list:
    """Loops through the list of users, if the user exists assign
    it to a variable curr_user, if not create a user, add it to the list
    and assign it's dictionary to the curr_user variable"""
    if str(user["username"]).lower() == username.lower():
        print("Welcome back") # need to change to a diff message
        curr_user = user # assigning a dictionary to be able to update the values later
        break
    else:
        curr_user = gl.User(username)
        user_list.append(curr_user.add_user())
        curr_user = curr_user.add_user() # assigning a dictionary to be able to update the values later
        print("Welcome") # need to change to a diff message
        break


# generating a list of possibilities
possibilities = []
for i in range(1): # current state for easier testing
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

# create a check of current score, if higher assign new high score

print(f"\n\tNumber of attempts: {attempts}"
      f"\n\t Your score: {score}")