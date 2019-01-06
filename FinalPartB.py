#Kelsi Fulton
#Final Exam Part B

#List of gifts
myGifts = ['Partridge in a Pear Tree', 'Turtle Doves', 'French Hens', 'Calling Birds', 'Golden Rings', 'Geese a Laying', 'Swans a Swimming', 'Maids a Milking',\
           'Ladies Dancing', 'Lords a Leaping', 'Pipers Piping', 'Drummers Drumming']

#define ordinal function
def ordinal(x):
        value = str(x)  #converts value to string to use .endswith operation
        if value.endswith('11'): #if value ends with 11, print 'th' suffix
                return(value+'th')
        elif value.endswith('12'):  #if value ends with 12, print 'th' suffix w/ value
                return(value+'th')
        elif value.endswith('1'):  #if value ends with 1, print 'st' suffix w/ value
                return(value+'st')
        elif value.endswith('2'):  #if value ends with 2, print 'nd' suffix w/ value
                return(value+'nd')
        elif value.endswith('3'):  #if value ends with 3, print 'rd' suffix w/ value
                return(value+'rd')
        else:
                return(value+'th')  #if value ends with any other number, print 'th' suffix w/ value
 
#define main function                 
def main():
        for i in range(1, len(myGifts)+1, 1): #begins for loop 
                print('On the', ordinal(i), 'day of Christmas my true love sent to me:')  #prints first line w/ different ordinal
                if i == 1: #if statement to print "A Partridge in a Pear Tree"; only prints when i is 1
                        print('A', myGifts[0])
                
                for i in range(len(myGifts)-1, 0, -1): #for loop to print number of gifts along with gift
                        print(i+1, myGifts[i])
                        
                print('and a', myGifts[0]) #prints "and a Partridge in a Pear Tree"
                                
#call main function                       
main()

#confused on how to make each line appear one by one