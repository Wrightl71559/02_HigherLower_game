# component 11

# guess calculator

import math

for itm in range(0,4):  # loop component for easy testing

    low = int(input("Please enter a low number "))  # use intcheck
    high = int(input("Please enter a high number")) # use intcheck

    range = high - low + 1
    max_raw = math.log2(range)  # finds maximum number of guesses using binary search
    max_upped = math.ceil(max_raw)  # rounds up
    max_guesses = max_upped + 1
    print("You have {} guesses".format(max_guesses))

    print()
