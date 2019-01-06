#Kelsi Fulton
#this is my code to print the appropriate message when various email
#addresses are entered

#asks user to input an email address
email = input('Enter an email address: ')

#if there is only 1 @ sign in the email, continue
if email.count('@') == 1:
    
    #if there is at least one period in the email, continue
    if email.count('.') >= 1:
        
        #if the first character is alphanumeric, continue
        if email[0].isalnum() == True:
            
            #if the email ends with. edu, then print appropriate message
            if email.endswith('.edu'):
                print('This is an educational email address.')
            
            #if the email ends with .com, then print appropriate message
            elif email.endswith('.com'):
                print('This is a commercial email address.')
            
            #if email ends with .org, then print appropriate message
            elif email.endswith('.org'):
                print('This is an organizational email address.')
            
            #emails ending with anything else are invalid
            #print appropriate message
            else:
                print('This is an unknown email address.')
                
        
        #emails that don't begin w/ an alphanumeric character are invalid
        #print appropriate message
        else:
            print('This is an unknown email address.')
            
    
    #emails that don't have at least one period are invalid
    #print appropriate message
    else:
        print('This is an unknown email address.')
      

#emails that have more than 1 @ sign are invalid, print appropriate message
else:
    print('This is an unknown email address.') 
   
    