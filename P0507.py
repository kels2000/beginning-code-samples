#Kelsi Fulton
#P0507
#This is my code to create a BMI chart.

#formats indentation in top left corner
print('   |', end='')
#formats top line to print weight by 10
for row in range(100, 261, 10):
    print(row, end='|')
#formatting: prints line underneath weights
print('\n------------------------------------------------------------------------')

#formats first column to print height in inches by 2
for col in range(54, 85, 2):
    print('%d ' % col, end='|')
    #formats output to print correctly for each row/column
    for row in range(100, 261, 10):         
        #BMI calculator
        bmi = (703 * ((row)/(col**2)))
        #classifies BMI 
        if bmi < 18.5:
            bmi = 'U'
        elif int(bmi) < 25:
            bmi = "N"
        elif int(bmi) < 30:
            bmi = "O"
        else:
            bmi = "X"        
        #prints BMI classification for each height/weight combination
        print(' %s '%(bmi), end='|')
    #new line to format correctly
    print()
