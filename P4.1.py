summation = 0
i = 2
while i <= 100:
    summation = summation + i
    i = i + 2 
print('summation = %d' % summation)

summationB = 0
i_B = 1
count = 3
while i_B <= 100:
    summationB = summationB + i_B
    i_B = i_B + count
    count = count + 2 
    
print('The sum of all squares is %d' % summationB) 

i_C = 0
power = 0
while i_C <= 20:
    power = 2 ** i_C
    i_C = i_C + 1
    print(power)
    

summationD = 0
a = int(input('Please enter an odd number: '))
b = int(input('Please enter another odd number: '))

while a <= b:
    summationD = summationD + a
    a = a + 2
print('summation = %d' % summationD)