#Kelsi Fulton
#P0401
#get the change due from user
change = int(input('Enter the change due (0-99): '))

#initialize the # of quarters, dimes, nickels, and pennies
Q = 0
D = 0
N = 0
P = 0

#subtract quarters until the change dues is less than 25
while change >= 25:
    Q = Q + 1
    change = change - 25
    
#subtract dimes until the change dues is less than 10
while change >= 10:
    D = D + 1
    change = change - 10

#subtract nickles until the change dues is less than 5
while change >= 5:
    N = N + 1
    change = change - 5
    
#whatever is left are pennies
P = change

#print results
print('Q = %d, D = %d, N = %d, P = %d' % (Q, D, N, P))
