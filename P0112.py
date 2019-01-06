#P0112
#Kelsi Fulton
#This is my code to print the area code, the first & last digit and the sum of the last four digits of a telephone number.

myNumber = '(313)-600-2509' 
digit1 = myNumber[1] #assign all necessary digits to separate variables
digit2 = myNumber[2]
digit3 = myNumber[3]

digit7 = myNumber[10]
digit8 = myNumber[11]
digit9 = myNumber[12]
digit10 = myNumber[13]

one = int(digit7) #converts digits into integers in order to add them
two = int(digit8)
three = int(digit9)
four = int(digit10)

lastFour = one+two+three+four #calculates sum of last four digits

print('The area code is', digit1 + digit2 + digit3 +'.')  #prints the area code
print('The first digit of the number is', digit1 +'.')  #prints the first digit of the phone number
print('The last digit of the number is', digit10 +'.')  #prints the last digit of the phone number
print('The sum of the last four digits is ' + str(lastFour) +'.') #prints sum of last four digits