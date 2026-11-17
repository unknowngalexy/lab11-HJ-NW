#https://github.com/unknowngalexy/lab11-HJ-NW.git
#Partner 1: Hyrum Johnston
#Partner 2: Ningxuan Wang

import math

def square_root(a):
    if a < 0:
        raise ValueError("Square root cannot take a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a,b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid logarithm")
    return math.log(b,a)

def exp(a,b):
    return a ** b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def logarithm(a, b): 
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Logarithm arguments must be positive and base cannot be 1.")
    return math.log(b, a) 

def exponent(a, b): 
    return a ** b

