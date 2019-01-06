#Kelsi Fulton
#Test - Part II

daysOfTheWeek = 'SMTWRFA' #given string 

currentDay = int(input("Enter today's day (0-6): "))  #asks user for todays day
daysInTheFuture = int(input('Enter some number of days in the future: '))  #asks user for some # of days in the future

futureDay = (currentDay + daysInTheFuture) % 7 #formula to calculate future days

#formatted string to give correct output
output = 'Today is ' + str(daysOfTheWeek[currentDay]) + '. ' + str(daysInTheFuture) + ' days from now will be ' + str(daysOfTheWeek[futureDay]) + '.'   
print(output)
