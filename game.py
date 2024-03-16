import game_library as gl

#generating a list of possibilities

possibilities = []
for i in range(1, 101):
    possibilities.append(i)

winning_number = gl.target_number(possibilities)

#building user input and results

#assigning a guess anc checking if the number is correct
while True:
    guess = gl.user_guess()
    active = gl.check_results(guess, winning_number)
    if active == False:
        break