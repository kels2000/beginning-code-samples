print('\nPart D')
#initialize count variable to count # of numbers
count = 0
#iterate through each character of the string
for number in userStr:
    #make a decision about whether or not to print the character
    if number.isdigit():
        #add 1 to count
        count = count + 1
#print # of numbers
print(count)

print('Part E')
#iterate through position of characters in string
for index in range(0, len(userStr)):
    #make a decision about whether or not to print the character position
    if userStr[index] in 'aeiouAEIOU':
        print(index, end='')