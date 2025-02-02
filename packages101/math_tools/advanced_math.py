# Packages 101 - Math_tools package creation - Advanced math tools
## Function to calculate the factorial of a number
def factorial(num):
    if num < 0:
        raise ValueError('Factorial is not defined for negative numbers.')
    if num == 0 or num == 1: return 1
    return num * factorial(num -1)
    

## Funtion to find the square root of a number
def square_root(num):
    if num < 0:
        raise ValueError('It is impossible to compute the square root of a negative number')
    from math import sqrt
    return sqrt(num)

## Function to calculate the exponent of a number
def power(base,exponent):
    return num1 ** num2

## Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0: 
            return False
        i += 6
        return True
        