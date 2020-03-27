# Component 5

# set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

SECRET = 7
GUESSES_ALLOWED = 4

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess the number ")) # Replace with function call

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You have already guessed that number! Please try again. "
              "You still have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

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
