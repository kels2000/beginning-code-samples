print('   |', end='')
for row in range(100, 261, 10):
    print(row, end='|')
print('\n------------------------------------------------------------------------')
for col in range(54, 85, 2):
    print('%d ' % col, end='|')
    for row in range(100, 261, 10):         
        bmi = (703 * ((row)/(col**2)))
        if bmi < 18.5:
            bmi = 'U'
        elif int(bmi) < 25:
            bmi = "N"
        elif int(bmi) < 30:
            bmi = "O"
        else:
            bmi = "X"        
        print(' %s '%(bmi), end='|')
    print()
