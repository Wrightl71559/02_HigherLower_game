# full program

# modules
import math
import random

# integer checking function


def int_check(question, low=None, high=None):

    # Error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter aqn integer that is less than or " \
                "equal to {}".format(high)
    else:
        error = "Whoops please enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

# statement generator function


def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print


# main routine

# Introduction

print("Welcome to the Higher Lower game")
print()
print("Your goal is to guess a secret number within a certain amount of guesses")
print()
print("You can choose how many rounds you want to play and the numbers you would like to guess between")
print()
print("At the end of the game your best, worst, and average score will be displayed")
print()
print("Good Luck!!")
print()


keep_going = ""
while keep_going == "":

    rounds = int_check("How many rounds would you like to play?  ", 1)
    lowest = int_check("Please enter a low number ")
    highest = int_check("Please enter a high number ", lowest + 1)
    range = highest - lowest + 1
    max_raw = math.log2(range)  # finds maximum number of guesses using binary search
    max_upped = math.ceil(max_raw)  # rounds up
    max_guesses = max_upped + 1
    print("You have {} guesses".format(max_guesses))


    game_stats = []
    already_guessed = []

    num_won = 0
    rounds_played = 0

    while rounds_played < rounds:
        print("Round {}".format(rounds_played + 1))

        guess = ""
        guesses_left = max_guesses
        secret = random.randint(lowest, highest)

        while guess != secret and guesses_left >= 1:

           guess = int_check("Guess the number ", lowest, highest)
           if guess in already_guessed:
                print("You have already guessed that number! Please try again. "
                "You still have {} guesses left".format(guesses_left))
                continue
           guesses_left -= 1
           already_guessed.append(guess)


           # if user has guess left
           if guesses_left >= 1:

                if guess > secret:
                    hl_statement("vv Too high, guess a lower number vv", "v" )
                    print("you have {} guesses left".format(guesses_left))
                elif guess < secret:
                    hl_statement("^^ Too low, guess a higher number ^^", "^")
                    print("you have {} guesses left".format(guesses_left))

            # if user is out of guesses
           else:
                if guess < secret:
                    print("Too low")
                elif guess > secret:
                    print("To high")

        if guess == secret:
            # if user has guessed right the first time...
            if guesses_left == max_guesses - 1:
                hl_statement("** Amazing! You got it first try **", "*")
                num_won += 1
            # if user has had more than one guess
            else:
                hl_statement("** Congratulations! You guessed the number **", "*")
                print("you had {} guesses left".format(guesses_left))
                num_won += 1
        else:
            print("Sorry, you have no guesses left. Game Over")
            guesses_left -= 1 # Penalty point for losing

        game_stats.append(max_guesses - guesses_left)
        print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
        rounds_played += 1
        already_guessed = []

    # print each rounds outcome...
    print()
    print("*** Game Scores ***")
    list_count = 1
    for item in game_stats:

        # indicates if game has been won or lost
        if item > max_guesses:
            status = "lost"
        else:
            status = "won"

        print("Round {}: {} ".format(list_count, item))
        list_count += 1

    # Calculate (and then  print) statistics
    game_stats.sort()
    best = game_stats[0]    # first item in sorted list
    worst = game_stats[-1]  # last item in sorted list
    average = sum(game_stats)/len(game_stats)

    print()
    print("*** Summary Statistics ***")
    print("Best: {}".format(best))
    print("Worst: {}".format(worst))
    print("Average: {:.2f}".format(average))

    print()
    keep_going = input("Press <enter> to play again or any key to quit ")
    print()

print("Thank you for playing. Good bye")
