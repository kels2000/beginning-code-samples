#Kelsi Fulton
#P0702 - Metric Converter

def menu():
    print('1. Miles -> Kilometers')
    print('2. Kilometers -> Miles')
    print('3. F -> C')
    print('4. C -> F')
    print('5. lb -> kg')
    print('6. kg -> lb')
    print('7. quit')
    choice = int(input('Enter your choice: '))
    return choice

def miToKm():
    miles = float(input('Please enter the distance in miles: '))
    km = miles * 1.609
    print('%.2f mi -> %.2f km' % (miles, km))
    
def kmToMi():
    km = float(input('Please enter the distance in kilometers: '))
    miles = km * 0.6214
    print('%.2f km -> %.2f mi' % (km, miles))  
    
def fToC():
    f = float(input('Please enter the temperature in degrees F: '))
    c = (f - 32)*.5556
    print('%.2f F -> %.2f C' % (f, c))
    
def cToF():
    c = float(input('Please enter the temperature in degrees C: '))
    f = (c * 1.8) + 32
    print('%.2f C -> %.2f F' % (c, f))
    
def lbToKg():
    lb = float(input('Please enter the weight in pounds (lbs): '))
    kg = lb * .4536
    print('%.2f lbs -> %.2f kg' % (lb, kg))

def kgToLb():
    kg = float(input('Please enter the weight in kilograms (kg): '))
    lb = kg * 2.205
    print('%.2f kg -> %.2f lbs' % (kg, lb))
    
def main():
    choice = menu()
    while choice < 1 or choice > 7:
        print('Error')
        print()
        choice = menu()    
    while 1 < choice < 7:
        if choice == 1:
            miToKm()
            print()
            choice = menu()
        elif choice == 2:
            kmToMi()
            print()
            choice = menu()
        elif choice == 3:
            fToC()
            print()
            choice = menu()
        elif choice == 4:
            cToF()
            print()
            choice = menu()
        elif choice == 5:
            lbToKg()
            print()
            choice = menu()
        elif choice == 6:
            kgToLb()
            print()
            choice = menu()
        elif choice == 7:
            print('Goodbye!')
            quit()
    
        
main()
        