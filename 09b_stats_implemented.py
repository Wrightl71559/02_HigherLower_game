# Component 9

# end game stats

# TO DO
# set up Game Play list with each rounds results
# Set up average, best and worst scores

SECRET = 7
GUESSES_ALLOWED = 4
rounds = int(input("How many rounds? "))    # replace with int check
game_stats = []

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
        guesses_left -= 1 # Penalty point for losing

    game_stats.append(GUESSES_ALLOWED - guesses_left)
    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1

# print each rounds outcome...
print()
print("*** Game Scores ***")
list_count = 1
for item in game_stats:

    # indicates if game has been won or lost
    if item > GUESSES_ALLOWED:
        status = "lost"
    else:
        status = "won"

    print("Round{}: {}".format(list_count, item))
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
