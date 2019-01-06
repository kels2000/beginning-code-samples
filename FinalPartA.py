#Kelsi Fulton
#Final Exam Part A

def ordinal():  #define ordinal function
    value = 0  #initialize value to start loops
    while value >= 0: #begin loop for ordinals
        value = int(input('Enter a number: ')) #prompts user for number
        while value < 0: #begin loop for sentinel value
            print('Goodbye!')  #prints goodbye output
            quit() #quits program
        value = str(value)  #converts value to string to use .endswith operation
        if value.endswith('11'): #if value ends with 11, print 'th' suffix
            print(value+'th')
            value = int(value)
        elif value.endswith('12'):  #if value ends with 12, print 'th' suffix w/ value
            print(value+'th')
            value = int(value)      #set value back to an integer for loop        
        elif value.endswith('13'):  #if value ends with 13, print 'th' suffix w/ value
            print(value+'th')
            value = int(value)     #set value back to an integer for loop
        elif value.endswith('1'):  #if value ends with 1, print 'st' suffix w/ value
            print(value+'st')
            value = int(value)     #set value back to an integer for loop
        elif value.endswith('2'):  #if value ends with 2, print 'nd' suffix w/ value
            print(value+'nd')
            value = int(value)     #set value back to an integer for loop
        elif value.endswith('3'):  #if value ends with 3, print 'rd' suffix w/ value
            print(value+'rd')
            value = int(value)     #set value back to an integer for loop
        else:
            print(value+'th')  #if value ends with any other number, print 'th' suffix w/ value
            value = int(value)

#define main function         
def main():
    print('Welcome to the ordinal converter program') #print greeting
    print('Enter a negative value to quit.')  #prints instructions    
    ordinal() #calls ordinal function
    
main() #calls main function