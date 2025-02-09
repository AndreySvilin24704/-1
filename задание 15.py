import math
centimeters = float(input())
inches = centimeters / 2.54
feet = inches / 12
yards = feet / 3
miles = yards / 1760
print(round(yards, 2), 'ярдов')
print(round(miles, 6), 'мили')
print(round(feet, 2), 'футов')
print(round(inches, 2), 'дюймов')



