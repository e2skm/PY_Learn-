# Exception Handling 2- Simple division
num1, num2, result = 0.0, 0.0, 0.0
## Infinte loop to ensure user enters two numbers and the denominator != 0
while True:
    try:
        ### Prompt user to enter two numbers
        print('Enter the first number (Numerator)')
        num1 = float(input())
        print('Enter the second number (Denominator)')
        num2 = float(input())
        result = round((num1 / num2),2) ### 
    except ZeroDivisionError:
        print('Error you cannot divide a number by 0')
    except ValueError:
        print('Error for division please enter two numbers')
    else:
        print(f'{num1} / {num2} = {result}')
        break