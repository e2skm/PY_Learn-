# Packages 101 - Math_tools package creation - Basic math tools
## Fuction to add two numbers
def add(num1,num2):
    return num1 + num2

## Fuction to subtract two numbers
def subtract(num1,num2):
    return num1 - num2

## Fuction to multiply two numbers
def multiply(num1,num2):
    return num1 * num2

## Fuction to divide two numbers
def divide(num1,num2):
    if num2 == 0 and num1 != 0:
        num1, num2 = num2, num1 ## Swap numbers to aviod zero division error (hopefully the first number is not zero as well)
        print(f'To avoid zero divison error the value of the denominator has been modified to {num2}')
    else:
        print('To avoid zero divison error the value of the denominator has been modified to 1')
        num2 == 1    
    return num1 / num2

## Function to determine whether a number is even, odd or a float
def is_even_or_odd(num):
    num = round(num)
    if num % 2 == 0:
        print(f'The number {num} is even.')
    else:
        print(f'The number {num} is odd.')   

## Function to determine which number is greater out of two numbers       
def compare(num1,num2):
    if num1 > num2:
        print(f'The first number {num1} is greater than the second number {num2}')   
    elif num1 < num2:
        print(f'The second number {num2} is greater than the first number {num1}') 
    else:
        print(f'Both numbers are equal')              