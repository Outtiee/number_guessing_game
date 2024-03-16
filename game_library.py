# importing choice() method to be able to generate a random number
from random import choice



#creating necessary methods

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
            print(f"How did you know I was thinking about the number {winning_number}?")
            return False
        elif int(guess) > winning_number:
            print("Try guessing a lower number.")
        else:
            print("Try guessing a bigger number.")
    except ValueError:
        print("Please enter a number.")