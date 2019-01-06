#Kelsi Fulton
#P0804
#This is my code to generate a fortune for the user

#import random to use randint
import random

#define function to pick sentence
def sentence1():
    #generates a random number based on the # of sentence options
    x = random.randint(1, 4)
    #when x is 1, it prints the first option
    if x == 1: 
        print('A Morehouse man')
    #when x is 2, it prints the second option
    elif x == 2:
        print('A flamboyant old man')
    #when x is 3, it prints the third option
    elif x == 3:
        print('A tall, dark and handsome supermodel')
    #when x is 4, it prints the fourth option
    else:
        print('A nutty professor')

#define function to pick sentence
def sentence2():
    #generates a random number based on the # of sentence options
    x = random.randint(1, 4)
    #when x is 1, it prints the first option
    if x == 1: 
        print('with a wart on his nose')
    #when x is 2, it prints the second option
    elif x == 2:
        print('carrying a dog')
    #when x is 3, it prints the third option
    elif x == 3:
        print('missing a few teeth')
    #when x is 4, it prints the fourth option
    else:
        print('dressed to impress')    

#define function to pick sentence        
def sentence3():
    #generates a random number based on the # of sentence options
    x = random.randint(1, 4)
    #when x is 1, it prints the first option
    if x == 1: 
        print('will ask you to dance.')
    #when x is 2, it prints the second option
    elif x == 2:
        print('will offer you a hamburger.')
    #when x is 3, it prints the third option
    elif x == 3:
        print('wants to be your friend.')
    #when x is 4, it prints the fourth option
    else:
        print('will take all your money.')  

#define function to pick sentence        
def sentence4():
    #generates a random number based on the # of sentence options
    x = random.randint(1, 4)
    #when x is 1, it prints the first option
    if x == 1: 
        print("But don't worry about it.")
    #when x is 2, it prints the second option
    elif x == 2:
        print('Try not to lose sleep over it')
    #when x is 3, it prints the third option
    elif x == 3:
        print('This could be your lucky day!')
    #when x is 4, it prints the fourth option
    else:
        print('Just tell him what you think.') 

#main function to call the sentence functions        
def main():
    sentence1()
    sentence2()
    sentence3()
    sentence4()

main()