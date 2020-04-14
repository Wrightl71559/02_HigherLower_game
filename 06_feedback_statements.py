# component 6
# prints formatted statements to make feedback easier for the user to read

def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

# Main Routine

too_low = hl_statement("^^ Too low, guess a higher nmuber ^^", "^")

print()
too_high = hl_statement("vv Too high, guess a lower number vv", "v")

print()
duplicate = hl_statement("!! You have already guessed that number! Please try again !!", "!")

print()
well_done = hl_statement("** Congratulations you guessed the number **", "*")

print()
start_round = hl_statement("## Round 1 of 3 ##", "#")

