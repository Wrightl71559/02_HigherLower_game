# component 8

# set up round and win counters
# update feedback statements

SECRET = 7
GUESSES_ALLOWED = 4
rounds = 3


num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    while guess != SECRET and guesses_left >= 1:

        guess = int(input("Guess the number ")) # Replace with function call
        guesses_left -= 1

        # if user has guess left
        if guesses_left >= 1:

            if guess > SECRET:
                print("Too high, guess a lower number")
                print("you have {} guesses left".format(guesses_left))
            elif guess < SECRET:
                print("Too low, guess a higher number")
                print("you have {} guesses left".format(guesses_left))
        # if user is out of guesses
        else:
            if guess < SECRET:
                print("Too low")
            elif guess > SECRET:
                print("To high")

    if guess == SECRET:
        # if user has guessed right the first time...
        if guesses_left == GUESSES_ALLOWED - 1:
            print("Amazing! You got it first try.")
            num_won += 1
        # if user has had more than one guess
        else:
            print("Congratulations! You guessed the number.")
            print("you had {} guesses left".format(guesses_left))
            num_won += 1
    else:
        print("Sorry, you have no guesses left. Game Over")

    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1
