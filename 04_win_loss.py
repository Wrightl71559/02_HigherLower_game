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
        elif guess < SECRET:
            print("Too low, guess a higher number")
        else:
            print ("Amazing! You guessed the number")
