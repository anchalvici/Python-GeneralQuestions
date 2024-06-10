# The math module contains the gcd function
import math


#Calculating the gcd of 2 numbers.
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
        
x=10
y=18

print(f"The computed GCD of {x} and {y} is {gcd(100,3)}."