#P4.5
#write a program that reads a set of floating point values. Ask the
#user to enter the values then print
# - the average of the values
# - the smallest of the values
# - the largest of the values
# - the range, that is the difference between the smallest and the largest

#initialize summation, count, largest & smallest values
summation = 0
count = 0
smallest = 0
largest = 0

#get the first value from user
userInput = input('Enter a value ("quit" to quit): ')

#set smallest and largest to the first value entered by the user
if userInput != 'quit':
    data = float(userInput)
    smallest = data
    largest = data
#loop until the user enters 'quit' (FYI, 'quit' is called a "sentinel value")
while userInput != 'quit':
    data = float(userInput)
    #add to the suumation
    summation = summation + data
    #update smallest and largest if necessary
    if data < smallest:
        smallest = data
    if data > largest:
        largest = data
    #increment the count (keep track of # of data points entered)
    count = count + 1
    #get new input from user
    userInput = input('Enter a value ("quit" to quit): ')
#calculate the average and range
average = summation/count
dataRange = largest - smallest

#print average, smallest, largest and range
print('average = %.2f, smallest = %.2f, largest = %.2f, range = %.2f' \
      % (average, smallest, largest, dataRange))