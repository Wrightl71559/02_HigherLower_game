# ask user for a high number and a low number
# check that input is valid - lowest, highest, guess


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





# Main routine

lowest = int_check("Please enter a low number ", )
highest = int_check("Please enter a high number ", lowest + 1)
guess = int_check("Guess the number ", lowest, highest)
rounds = int_check("Rounds ", 1)