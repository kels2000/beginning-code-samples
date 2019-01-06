#Kelsi Fulton
#P0403
#Your task is to write a program that does just that.  The user enters the 
#scaling factor used to scale the drawing.  You should verify that this 
#scaling value is >= 1.  If not, the program should reprompt the user for a 
#valid scaling factor.  The output of the program is simply the scaled box.

#ask user to input scaling factor
scalingFactor = int(input('Please enter a number >= 1 to scale the box: '))

#while the scaling factor is less than one,
while scalingFactor < 1:
    
    #show error, ask for correct scaling factor
    scalingFactor = int(input('Error - Enter a number greater than/equal to 1: '))

#create variable for the space to align top lines 
topSpace = ' '

#create variable to scale top lines
topLines = scalingFactor * '-'

#create variable to scale the space in the middle
middleSpace = scalingFactor * ' '

#format output to print top lines
print(topSpace, topLines)

#for scale in 0-scalingFactor,
for scale in range(scalingFactor):
    
    #print vertical lines with correct # of spaces between them & correct
    #number of total lines
    print('|', middleSpace, '|')

#format output to print bottom lines   
print(topSpace, topLines)