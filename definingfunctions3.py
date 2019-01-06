#Write a program that randomly picks a # from 1-20 and give the user
#5 tries to guess the #. The program telle the user "higher" or "lower"
#as appropriate after each guess.

import random
#function to get the user's guess
def getUserGuess():
    x = int(input('Please enter a guess from 1 to 20: '))
    return x

def main():
    #generate the random #
    computerNumber = random.randint(1, 20)
    
    #initialize the # of guesses to zero
    numGuesses = 0
    userGuess = -1 
    print(computerNumber)
    
    #loop 5 times until the user guesses right
    while numGuesses < 5 and computerNumber != userGuess:
        #get the user's guess
        userGuess = getUserGuess()
        #compare to generated number
        #tell the user if higher or lower or if they got it right
        if userGuess > computerNumber:
            print('Lower!')
        elif userGuess < computerNumber:
            print('Higher!')
        else:
            print('Good job, you got it!')
        #adjust guess and iterations apporopriately
        numGuesses = numGuesses + 1
    if numGuesses == 5 and userGuess != computerNumber:
        print(':(')
main()