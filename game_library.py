# importing choice() method to be able to generate a random number
from random import choice

# creating a class to call for creating a new user

class User:
    def __init__(self, username, score=0):
        self.username = username
        self.score = score

# creating necessary methods to play the game

def target_number(possibilites):
    """Generates a random number"""
    winning_number = choice(possibilites)
    print("Can you guess the number I am thinking of between 1 and 100?")
    return winning_number


def user_guess():
    """Prompts user to make a guess and return the value
    of the guess"""
    guess = input("I'm guessing you're thinking about the number ")
    return guess


def check_results(guess, winning_number):
    """Method that checks the result and prints out the appropriate message"""
    try:
        if int(guess) == winning_number:
            print(f"\nI was thinking about the number {winning_number}!")
            return False
        elif int(guess) > winning_number:
            print("That is incorrect. Here's a hint, try guessing a lower number.")
            # attempts +1, score calc
        else:
            print("That is incorrect. Here's a hint, try guessing a bigger number.")
            # att +1, score calc
    except ValueError:
        print("Please enter a number.")
        return "error"