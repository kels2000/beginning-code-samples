#P0116
#Kelsi Fulton
#This is my code to prompt the user to input a blood pressure reading and to print the systolic & diastolic value.

x = input('Please enter the blood pressure as SSS/DD: ') #prompts user to enter blood pressure reading
s1 = x[0]  #assigns indexes to variables in order to print them later
s2 = x[1]
s3 = x[2]
d1 = x[4]
d2 = x[5]

sysVal = s1 + s2 + s3  #assigns sysVal to the correct sequence of indexes
diaVal = d1 + d2  #assigns diaVal to the correct sequence of indexes

print('The systolic value is', sysVal +'.')  #prints the systolic value 
print('The diastolic value is', diaVal + '.')  #prints the diastolic value
