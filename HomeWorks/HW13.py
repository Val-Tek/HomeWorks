def game():
    print("Welcome to game. I want you to hold a number between 1 and 100")
    # parameters:
    l_limit = 1
    h_limit = 100
    found = False
    count = 0
    while not found:
        guess = int((l_limit + h_limit) / 2)
        answer = input("Is your number {0}? (C:correct, L:lower, H:higher)  Your Answer: ".format(guess))
        count += 1
        if answer.upper() == "C":
            print('I found it in {0} guesses :) '.format(count))
            found = True
        if answer.upper() == 'L':
            h_limit = guess
        if answer.upper() == "H":
            l_limit = guess
    print("Game over")

