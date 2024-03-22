import game_library as gl
import json

username = input("Hello. What is your username? ").lower()

with open("userbase.json", "r") as file:
    data = json.load(file)
user_list = data

# check if user exists, if not create a new one

for user in user_list:
    if username in user["username"]:
        curr_user = user
        break
    else:
        curr_user = gl.User(username).add_user()
        

if curr_user not in user_list:
    print(f"Welcome {username}!")
    user_list.append(curr_user)
else:
    print(f"Welcome back {username}")
    print(f"Current high score: {curr_user["score"]}")



print("Game Menu:"
      "\t\n1. Start new game"
      "\t\n2. Show player scores"
      "\t\n3. Exit the game")


# creating a menu system

action = input("Select: ")
match action:
    case "1":
        # generating a list of possibilities
        possibilities = []
        for i in range(1, 101): 
            possibilities.append(i)
        winning_number = gl.target_number(possibilities)
        attempts = 1
        score = 10_000

        # guess loop and altering the score accordingly
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

                
        data = json.dumps(user_list)
        with open("userbase.json", "w") as file:
            file.write(data)
            file.close()

        # checking whether new result is a high score
            
        if curr_user["score"] < score:
            print(f"Congratulations, you got a new high score!")
            print(f"\tNew high score: {score}")        
            index = user_list.index(curr_user)
            user_list[index] = {"username": username, "score": score}

        print("\nGame results: ")
        print(f"\n\tNumber of attempts: {attempts}"
            f"\n\t Your score: {score}")
    case "2":
        print(f"\n{user["username"]}: {user["score"]}")
    case "3":
        quit()



data = json.dumps(user_list)
with open("userbase.json", "w") as file:
    file.write(data)
    file.close()