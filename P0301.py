#Kelsi Fulton
#P0301
#This is my code to ask for gender, height & weight, then print the correct tuxedo/dress size.

gender = input('Please enter your gender (male or female): ')  #asks user to input gender

if (gender == 'male'):  #conditional for gender choice
    height = float(input('Please enter your height in inches: ')) #asks user to input height
    if height < 55:  #conditional for height input - prints tuxedo size needed
        print('You need a short tuxedo.')
    else:
        if height > 60:
            print('You need a tall tuxedo.')
        else:
            print('You need a medium tuxedo.')
else:
    weight = float(input('Please enter your weight in pounds: ')) #conditional for weight input - prints dress size needed
    if weight < 110:
        print('You need a small dress.')
    else:
        if weight > 150:
            print("You need a large dress.")
        else:
            print("You need a medium dress.")
    