#Kelsi Fulton
# P1103.py
#
# The isMagicSquare() function
# accepts a 2D list and return a boolean indicating
# whether or not the 2D list forms a magic square.
# Assume that the provided 2D list is square (i.e.,
# number of rows is equal to number of columns)

def isMagicSquare(square):
    #calculate sum of rows
    rowTotal = 0
    i = 0
    for j in range(len(square)):
        rowTotal = rowTotal + square[i][j]
    
    #calculate sum of columns    
    colTotal = 0
    j = 0
    for i in range(len(square)):
        colTotal = colTotal + square[i][j]
    
   #calculate sum of diagonal    
    diagTotal1 = 0
    for i in range(len(square)):
        diagTotal1 = diagTotal1 + square[i][i]
    
    #set verify to false before you check
    verify = False
    
    #check if it is a real magic square
    if rowTotal == colTotal and rowTotal == diagTotal1 and diagTotal1 == colTotal:
        verify = True
    
    #returns verify     
    return verify
    
def main():
    #create 6 potential magic squares
    ms1 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    ms2 = [[4, 9, 2], [8, 1, 6], [3, 5, 7]]
    ms3 = [[8]]
    ms4 = [[52, 11, 85, 28], [88, 25, 51, 12], [21, 82, 18, 55], [15, 58, 22, 81]]
    ms5 = [[2, 3], [2, 3]]
    ms6 = [[23,6,19,2,15], [4,12,25,8,16], [10,18,1,14,22], [11,24,7,20,3], [17,5,13,21,9]]
    
    isMagic1 = isMagicSquare(ms1) 	#check magic square 1
    isMagic2 = isMagicSquare(ms2) 	#check magic square 2
    isMagic3 = isMagicSquare(ms3) 	#check magic square 3
    isMagic4 = isMagicSquare(ms4) 	#check magic square 4
    isMagic5 = isMagicSquare(ms5) 	#check magic square 5
    isMagic6 = isMagicSquare(ms6) 	#check magic square 6    
    
    
    #print results for magic square 1
    if isMagic1 == True:
        print('ms1 is magic!')
    else:
        print('ms1 is NOT magic!')
         
    #print resutls for magic square 2
    if isMagic2 == True:
        print('ms2 is magic!')
    else:
        print('ms2 is NOT magic!')
         
    #print results for magic square 3
    if isMagic3 == True:
        print('ms3 is magic!')
    else:
        print('ms3 is NOT magic!')
         
    #print resutls for magic square 4
    if isMagic4 == True:
        print('ms4 is magic!')
    else:
        print('ms4 is NOT magic!')
         
    #print results for magic square 5
    if isMagic5 == True:
        print('ms5 is magic!')
    else:
        print('ms5 is NOT magic!')
         
    #print resutls for magic square 6
    if isMagic6 == True:
        print('ms6 is magic!')
    else:
        print('ms6 is NOT magic!') 
        
main()
    

