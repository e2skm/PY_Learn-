# Comparision Opps - PY-learn projectn
## This program requires two numerical inputs, stores both numbers, Compares them and returns the which one is greater

compareAgain = True
numberOfComp = 0
while compareAgain == True:
    num1, num2 = 0, 0
    print('Please enter two numbers for basic comparison operations in python')
    for i in range(2):
        if i == 0:
            print(f'Enter the first number')
            num1 = float(input())
        else:
            print(f'Enter the second number')
            num2 = float(input())

    if (num1 > num2):
        print(f'The first number {num1} is greater than the second number: {num1} > {num2}')
    elif (num1 < num2):
        print(f'The second number {num2} is greater than the first number: {num2} >  {num1}')
    else:
       print(f'Both numbers are equal {num1} == {num2}')
     
    numberOfComp += 1  
    print(f'Would you like to compare numbers again Enter Yes/No alternatively Y or N')
    yesOrNo = str(input()).upper()
    if yesOrNo in ['N','NO']:
        print(f'Goodbye!! you made {numberOfComp} comparisions :)')
        compareAgain = False
      