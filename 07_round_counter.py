# component 7

# asks user for number of rounds they'd like to play
# counts number of rounds played
# tells user when all rounds have been played

rounds = int(input("How many rounds would you like to play? ")) # check with integer checker
rounds_played = 0

while rounds_played < rounds:
    print("Round {}".format(rounds_played+1))
    rounds_played += 1

print("You have reached the end of the game")
