# Component 4

# set up number of guesses
# count guesses taken
# if user runs out of guesses print "you lose"
# if user guesses secret number before guesses run out print "you win"

SECRET = 7
GUESSES_ALLOWED = 4

# initialise variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess the number "))  # Replace this with function call
    guesses_left -= 1

    # if user has guess left
    if guesses_left >=1:
        if guess > SECRET:
            print("Too high, guess a lower number")
        else:
            print("Too low, guess a higher number")

    # if user is out of guesses
    else:
        print("Sorry, you are out of guesses.")

if guess == SECRET:
    # if user has guessed right the first time...
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Amazing! You got it first try.")
        num_won += 1
    # if user has had more than one guess
    else:
        print("Congratulations! You guessed the number.")
        num_won += 1
