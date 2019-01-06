#Kelsi Fulton
#This is my code to determine pollen count & allergy warning level from
#user input.

#ask user to input pollen count for trees
trees = int(input('What is the pollen count from trees? '))

#when the trees' pollen count is between 0-14, set allergy level to low
if trees <= 14:
    level = 'Low'

#when the trees' pollen count is between 15-89, set allergy level to medium
elif trees <= 89:
    level = 'Medium'

#when the trees' pollen count is between 90-1499, set allergy level to high
elif trees <= 1499:
    level = 'High'

#when the trees' pollen count is 1500+, set allergy level to extremely high
else:
    level = 'Extremely High'
    
#ask user to input pollen count for grasses   
grasses = int(input('What is the pollen count from grasses? '))

#when the grasses' pollen count is between 0-4, set allergy level to low
#(if it isn't already)
if grasses <= 4 and level == 'Low':
    level = 'Low'
    
#when the grasses' pollen count is between 5-19, set allergy level to medium
#(if it isn't already)
elif grasses <= 19 and (level == 'Low' or level == 'Medium'):
    level = 'Medium'

#when the grasses' pollen count is between 20-199, set allergy level to high
#(if it isn't already)
elif grasses <= 199 and (level == 'Low' or level == 'Medium' or level == 'High'):
    level = 'High'

#when the grasses' pollen count is between 200+ set allergy level to extremely high
#(if it isn't already)
elif grasses >= 200 and (level == 'Low' or level == 'Medium' or level == 'High' or level == 'Extremely High'):
    level = 'Extremely High'

#ask user to input pollen count for weeds    
weeds = int(input('What is the pollen count from weeds? '))

#when the weeds' pollen count is between 0-9, set allergy level to low
if weeds <= 9 and level == 'Low':
    level = 'Low'

#when the weeds' pollen count is between 10-49, set allergy level to medium
#(if it isn't already)
elif weeds <= 49 and (level == 'Low' or level == 'Medium'):
    level = 'Medium'
    
#when the weeds' pollen count is between 50-499, set allergy level to high
#(if it isn't already)
elif weeds <= 499 and (level == 'Low' or level == 'Medium' or level == 'High'):
    level = 'High'

#when the grasses' pollen count is 500+, set allergy level to extremely high
#(if it isn't already)
elif weeds >= 500 and (level == 'Low' or level == 'Medium' or level == 'High' or level == 'Extremely High'):
    level = 'Extremely High'

#calculate total pollen count by adding the pollen counts together
total = trees + weeds + grasses

#print total pollen count
print('The total pollen count is', str(total) + '.')

#print allergy warning level
print('The allergy warning level is', str(level) + '.')