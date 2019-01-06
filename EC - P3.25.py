#Kelsi Fulton
#P3.25
#this is my code to compute taxes according to the table given on page 154

#created variables for each constant in the table given
SINGLE_TAX_LEVEL_ONE = .10
SINGLE_MAX_LEVEL_ONE = 8000

SINGLE_TAX_LEVEL_TWO = .15
SINGLE_MAX_LEVEL_TWO = 32000

SINGLE_TAX_LEVEL_THREE = .25

MARRIED_TAX_LEVEL_ONE = .10
MARRIED_MAX_LEVEL_ONE = 16000

MARRIED_TAX_LEVEL_TWO = .15
MARRIED_MAX_LEVEL_TWO = 64000

MARRIED_TAX_LEVEL_THREE = 8800 

#ask user to input relationship status (single/married)
status = input('Please input relationship status (single or married): ')

#ask user to input their income
income = float(input("Please input your taxable income: "))

#if they are single, follow sequence 
if status == 'single':
    #if the income is between 0 and the max. amount for the first tax bracket,
    if 0 <= income <= SINGLE_MAX_LEVEL_ONE:
        
        #multiply income by the % given to find tax
        tax = income * SINGLE_TAX_LEVEL_ONE
        
        #print output statement for tax amount
        print('Your taxes are $%.2f.' % tax)
    
    #if the income is between the max. amount for the first tax bracket 
    #and the max. amount for the 2nd tax bracket,
    elif income <= SINGLE_MAX_LEVEL_TWO:
        
        #find the difference by subtracting the max. amount for the first
        #tax bracket from user income 
        difference = income - SINGLE_MAX_LEVEL_ONE
        
        #multiply difference by the % given to find tax then add 800
        tax = (SINGLE_TAX_LEVEL_TWO * difference) + 800
        
        #print output statement for tax amount
        print('Your taxes are $%.2f.' % tax)
    
    #for amounts greater than the max. amount for the second tax bracket,
    else:
        
        #find the difference by subtracting the max. amount for the second
        #tax bracket from user income    
        difference = income - SINGLE_MAX_LEVEL_TWO
        
        #multiply difference by the % given to find tax then add 4400
        tax = (SINGLE_TAX_LEVEL_THREE * difference) + 4400
        
        #print output statement for tax amount
        print('Your taxes are $%.2f.' % tax)

#if they are married, follow sequence        
else:
    #if the income is between 0 and the max. amount for the first tax bracket,
    if 0 <= income <= MARRIED_MAX_LEVEL_ONE:
        
        #multiply income by the % given to find tax
        tax = income * MARRIED_TAX_LEVEL_ONE
        
        #print output statement for tax amount
        print('Your taxes are $%.2f.' % tax)
    
    #if the income is between the max. amount for the first tax bracket 
    #and the max. amount for the 2nd tax bracket,    
    elif income <= MARRIED_MAX_LEVEL_TWO:
        
        #find the difference by subtracting the max. amount for the first
        #tax bracket from user income        
        difference = income - MARRIED_MAX_LEVEL_ONE
        
        #multiply difference by the % given to find tax then add 1600
        tax = (MARRIED_TAX_LEVEL_TWO * difference) + 1600
        
        #print output statement for tax amount
        print('Your taxes are $%.2f.' % tax)
    
    #for amounts greater than the max. amount for the second tax bracket,
    else:
        
        #find the difference by subtracting the max. amount for the second
        #tax bracket from user income         
        difference = income - MARRIED_MAX_LEVEL_TWO
        
        #multiply difference by the % given to find tax then add 8800
        tax = (MARRIED_TAX_LEVEL_THREE * difference) + 8800
        
        #print output statement for tax amount
        print('Your taxes are $%.2f.' % tax)