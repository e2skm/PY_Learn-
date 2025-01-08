# Basic Math Opps - PY-learn projectn
## This program requires two numerical inputs, stores both numbers, performs basic mathematical operations and returns the result

numberOfMani = 0
manipulateAgain = True
while manipulateAgain == True:
    num1, num2 = 0, 0
    print('Please enter two numbers for basic mathematical operations in python')
    for i in range(2):
        if i == 0:
            print(f'Enter the first number')
            num1 = float(input())
        else:
            print(f'Enter the second number')
            num2 = float(input())

    sum = num1 + num2
    difference = num1 - num2
    modulus = num1 % num2
    product  = num1 * num2
    division = num1 / num2
    intDivision = num1 // num2

    print(f'The sum of {num1} + {num2} = {sum}')
    print(f'The difference of {num1} - {num2} = {difference}')
    print(f'The remainder(%) of {num1} / {num2} = {modulus}')
    print(f'The product of {num1} * {num2} = {product}')
    print(f'The division of {num1} / {num2} = {division}')
    print(f'The interger division of {num1} // {num2} = {intDivision}')

    numberOfMani += 1  
    print(f'Would you like to compare numbers again Enter Yes/No alternatively Y or N')
    yesOrNo = str(input()).upper()
    if yesOrNo in ['N','NO']:
        print(f'Goodbye!! you made {numberOfMani} manipluations :)')
        manipulateAgain = False