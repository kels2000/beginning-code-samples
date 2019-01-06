#Kelsi Fulton
#P0407
#Write a program that calculates the amount of money a person would earn 
#over a period of time if his or her salary is one penny the first day, 
#two pennies the second day, and continues to double each day. The program 
#should ask the user for the number of days. Display a table showing what 
#the salary was for each day, and then show the total pay at the end of the 
#period. The output should be displayed in a dollar amount, not the number 
#of pennies.

#initialize variables
days = 0
dayTotal = 0
salary = 0.01
total = 0

#get number of days from user
userInput = int(input('Please enter number of days: '))

#loop until days reach the input value
while days < userInput:
    #increment number of days for the table
    days = days + 1
    
    #add penny to salary to show each day's total pay
    dayTotal = dayTotal + salary
    
    #print current day and salary
    print('Day %d: $%.2f' % (days, salary))
    
    #doubles salary each day
    salary = salary * 2
    
    #calculates total pay
    total = total + dayTotal
    
#formatted output to give total    
print('---------------------', '\n'+'Total = $%.2f' % (total))
