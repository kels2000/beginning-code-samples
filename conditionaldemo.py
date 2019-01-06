total = 0.0
count = 0

largest = float(input("Enter a number (0 to quit):"))
inputStr = input("Enter a number (0 to quit):")
while largest != 0:
  num = float(inputStr) 
  if num > largest:
    largest = num
  inputStr = input("Enter a number (0 to quit):")
print('The largest value is:', largest,)

while numbers != 0:
  inputStr = input("Enter a number (0 to quit):")
  if numbers > 0:
    total = total + numbers
    count = count + 1
if count > 0:
    average = total/count

average = str(average)
print("The average of the values is", average,)


