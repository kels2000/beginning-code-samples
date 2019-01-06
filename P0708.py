#P0708 Sphere Geometry

import math

#circumference function
#accepts radius and returns circumference
def circumference(radius):
    c = 2 * math.pi * radius
    return c

#surface area function
#accepts a radius and circumference and returns the surface area
def surfaceArea(radius, circ):
    sa = 2 * radius * circ
    return sa

#volume function
#accepts a radius and surface area and returns the volume
def volume(radius, sa):
    vol = radius*sa/3
    return vol

#main
#ask user for a radius, then call the functions to 
#caluculate circumference, surface area and volume

def main():
    radius = float(input('Enter a radius: '))
    
    #calculate cirumference
    circ = circumference(radius)
    #calculate surface area
    sa = surfaceArea(radius, circ)
    #calculate volume
    v = volume(radius, sa)
    
    #print results
    print('The circumference is %.2f.' % circ)
    print('The surface area is %.2f.' % sa)
    print('The volume is %.2f.' % v)

main()