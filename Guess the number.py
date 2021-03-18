from random import randint

def guess(x):
    #variable for random numbers
    random_num = randint(1, x)
    #Placeholder for the user's guess
    your_guess = 0
    #Limits the user's guesses
    guess = 0
    guess_limit = 3
    #To break the loop
    out_of_guess = False

    print(f"Guess the number from 1 to {x}")
    while your_guess != random_num and not out_of_guess:
        #Checking the remaining guess
        if guess < guess_limit:
            your_guess = int(input("Enter your guess number:  "))\
            #If the guess is less than the random num
            if your_guess < random_num:
                print(f"{your_guess} is less than the secret number")
                guess += 1
            #If the guess is more than the random num
            elif your_guess > random_num:
                print(f"{your_guess} is more than the secret number")
                guess += 1
        #Stop users from guessing
        else:
            out_of_guess = True
    #Prints the outcome
    if out_of_guess:
        print("Out of guess sorry")
    else:
        print("You win!")

guess(10)