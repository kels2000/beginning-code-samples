#Kelsi Fulton
#P0710b - Kilometer Converter

#assign constant to a variable
MILES_CONSTANT =.6214

#define conversion function
def kmConversion(userInput):
    #conversion formula
    miles = userInput * MILES_CONSTANT
    #returns value for miles
    return miles    

#define main function
def main():
    #ask user to input km
    kilometers = float(input('Please enter a distance in kilometers: '))
    #calls conversion function
    miles = kmConversion(kilometers)
    #formatted output displays # of miles
    print('%.3f miles' % miles)    

#calls main function    
main()