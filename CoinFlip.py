from random import choice
again = 1
total_guess = 0
correct_guess = 0

while again > 0:
    inpt = input("Input H for Heads and T for Tails\n")
    outpt = choice(['Heads', 'Tails'])
    print(outpt)
    if (inpt == "T"):
        input = "Tails"
    else:
        inpt = "Heads"
    if (inpt == outpt):
        print("You Guessed it Correctly")
        total_guess += 1
        correct_guess += 1
    else:
        print("You Guessed it Wrong")
        total_guess += 1
    print("Total Guesses are " + str(total_guess) +
          " and correct guesses are " + str(correct_guess))
    again = int(input("Input 1 to play again and 0 to stop\n"))
        

