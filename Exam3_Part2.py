#Kelsi Fulton
#Exam 3 - Part 2
#This is my code to print pocket color when user inputs pocket number. 
 

#asks user to input a pocket number
pocket = int(input("Please enter a pocket number from 0-36: ")) 

#when the user's number isn't between 0-36, follow sequence until the
#user inputs the correct pocket number 
while pocket < 0 or pocket > 36: 
    #output error statement 
    print('Error: invalid value') 
    
    #asks user to input a new (and correct) pocket number
    pocket = int(input("Please enter a pocket number from 0-36: "))

#pocket 0 is green
if pocket == 0:
    #output corresponding color statement
    print('The pocket is green.')

#pockets 1-18 have specific rules    
if pocket < 19 and pocket > 0: 
    #if there is no remainder, it is even
    if pocket % 2 == 0:
        #output corresponding color statement
        print('The pocket is black.')
     #if there is a remainder, it is odd
    else:
        #output corresponding color statement
        print('The pocket is red.')

#pockets 19-36 have specific rules 
if pocket <= 36 and pocket >= 19:
     #if there is no remainder, it is even
    if pocket % 2 == 0:
        #output corresponding color statement
        print('The pocket is red.')
     #if there is a remainder, it is odd
    else:
        #output corresponding color statement
        print('The pocket is black.')    
        


