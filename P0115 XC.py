#P0115
#Kelsi Fulton
#This is my code that prompts the user for the year then prints the date of Easter Sunday for that year.

y = int(input('Please enter a year: ')) #prompts user to input a year

#calculates the date using Gauss' algorithm & assigns the numbers to variables
a = y%19  
b = y//100  
c = y%100  
d = b//4 
e = b%4  
g = (8 * b + 13)//25 
h = (19 * a + b - d - g + 15)%30
j = c//4
k = c%4
m = (a + 11 * h)//319
r = (2 * e + 2 * j - k - h + m + 32)%7
n = (h - m + r + 90)//25
p = (h - m + r + n + 19)%32


month = str(n) #assigns the variables n & p to new variables as strings
day = str(p)
date = month + '/' + day #assigns month & day format to new variable 

print('Easter Sunday falls on ' + date + ' in', str(y) + '.') #prints the date Easter falls on for the user-selected year.
