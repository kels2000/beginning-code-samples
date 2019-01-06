#Kelsi Fulton
#P0710a - Kilometer Converter

#assign constant to a variable
MILES_CONSTANT =.6214

#define conversion function
def kmConversion(userInput):
    #conversion formula
    miles = userInput * MILES_CONSTANT
    #formatted output displays # of miles
    print('%.3f miles' % miles)            

#define main function
def main():
    #ask user to input km
    kilometers = float(input('Please enter a distance in kilometers: '))
    #calls conversion function
    miles = kmConversion(kilometers) 

#calls main function    
main()

