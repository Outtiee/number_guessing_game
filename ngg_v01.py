"""This programs generates a random number between the values
of 0 and 100 and asks a user to guess it."""


#importing required methods and libraries
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

#generating a list of possibilities

possibilities = []
for i in range(1, 101):
    possibilities.append(i)

winning_number = target_number(possibilities)

#building user input and results

#assigning a guess anc checking if the number is correct
while True:
    guess = user_guess()
    active = check_results(guess, winning_number)
    if active == False:
        break