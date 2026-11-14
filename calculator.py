"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError("Square root cannot take a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    if b = 0: 
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def logarithm(a, b): 
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Logarithm arguments must be positive.")
    return math.log(b, a) 

def exponent(a, b): 
    return a ** b

