# Component 2
# compare users guess to secret number

SECRET = 7

guess = ""

while guess != SECRET:

    guess = int(input("Guess the number "))  # Replace this with function call

    if guess > SECRET:
        print("Too high, guess lower")
    elif guess < SECRET:
        print("Too low, guess a higher number")
    else:
        print ("Amazing! You guessed the number")
