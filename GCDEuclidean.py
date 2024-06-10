#The math module contains the gcd function
import math
#Calculating the gcd of 2 numbers.
x = 86
y = 44

while y:
    x,y = y, x%y

print(f"The computed GCD is {x}.")