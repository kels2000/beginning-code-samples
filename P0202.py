#Kelsi Fulton
#P0202

#asks user to input lengths & widths
length1 = float(input('Please enter the length of the first rectangle: '))
width1 = float(input('Please enter the width of the first rectangle: '))
length2 = float(input('Please enter the length of the second rectangle: '))
width2 = float(input('Please enter the width of the second rectangle: '))

#calculates areas
rect1 = length1 * width1
rect2 = length2 * width2

#decides what to print based on area calculations
if rect1 == rect2:
    print('The areas are the same.')
if rect1 > rect2:
    print('The area of the first rectangle is greater than the second rectangle.')
if rect2 > rect1:
    print('The area of the second rectangle is greater than the first rectangle.')

