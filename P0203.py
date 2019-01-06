#Kelsi Fulton
#This is my code to print a message based on the user's age.

#asks user to input age
age = int(input('Please enter your age: '))

#if the age is less than/equal to 1, print infant message
if age <= 1:
    print('You are an infant.')

#if the age is greater than 1 but less than 13, print child message
elif 1 < age < 13:
    print('You are a child.')
    
#if the age is greater than/equal to 13 but less than 20, print teen message
elif 13 <= age < 20:
    print('You are a teenager.')

#if the age is greater than 20, print adult message
else:
    print('You are an adult.')