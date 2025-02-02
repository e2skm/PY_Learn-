# Packages 101 - Math_tools package usage - main function
## Import specific user defined modules from package
import sys
import os

# Add the package directory to Python's search path
sys.path.append(os.path.abspath(r"C:\Users\itumeleng\Desktop\Python Programs\PY_LEARN PROJECTS\Package 101\math_tools"))
from math_tools import advanced_math,basic_math

## Prompt user for two numbers
while True:
    try:
        print('Kindly enter the First number')
        num1 = float(input())
        break
    except Exception:
        print('Error!! carefully follow these instructions')
while True:
    try:
        print('Kindly enter the Second number')
        num2 = float(input())
        break
    except Exception:
        print('Error!! carefully follow these instructions')        
        
## Perform basic functions
added = basic_math.add(num1,num2)
print(f'The result of adding {num1} and {num2} is {added}')
subtracted = basic_math.subtract(num1,num2)
print(f'The result of subtracting {num1} and {num2} is {subtracted}')
multiplied = basic_math.multiply(num1,num2)
print(f'The result of multiplying {num1} and {num2} is {multiplied}')
divided = basic_math.divide(num1,num2)
print(f'The result of dividing {num1} and {num2} is {divided}')
basic_math.is_even_or_odd(num1)
basic_math.is_even_or_odd(num2)
basic_math.compare(num1,num2)

## Perform advanced functions
numFact1 = advanced_math.factorial(num1)
print(f'The factorial of {num1} is {numFact1}')
numFact2 = advanced_math.factorial(num2)
print(f'The factorial of {num2} is {numFact2}')
sqrtNum1 = advanced_math.square_root(num1)
print(f'The square root of {num1} is {sqrtNum1}')
sqrtNum2 = advanced_math.square_root(num2)
print(f'The square root of {num2} is {sqrtNum2}')
pw = advanced_math.power(num1,num2)
print(f'The result of the base {num1} raised to the power of exponent {num2} is {pw}')
if advanced_math.is_prime(num1):
    print(f'{num1} is a prime number')
else:
    print(f'{num1} is not a prime number') 
if advanced_math.is_prime(num1):
    print(f'{num2} is a prime number')
else:
    print(f'{num2} is not a prime number')       