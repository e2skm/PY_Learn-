# Force Calculator  - PY-learn projectn
## Calculate force: by asking user to enter mass and accelaration or by randomising
## Import the random liabrarie to generate random variables for mass and acceleration
import random
## Create a variable for the loop continuation condition and loop
calculateForce = True
print('Welcome this program calculates the force applied to an object.')
while calculateForce == True:
    ### Create variables 
    optionMR = ''
    mass, acceration, appliedForce = 0.0, 0.0, 0.0
    print('Please enter M to enter Mass and Acceraration manually,R to Randomise Mass and Acceration or Q to Quit program')
    optionMR = str(input()).capitalize()
    ### Set control statements to control program's follow 
    if optionMR[0] in ['Q','Quit']:
        print('Thanks bye!! :)')
        break;
    elif optionMR[0] == 'M':
        for x in range(2):
            if x == 0:
                print('Please enter the Mass of the object')
                mass = float(input())
            else:
                print('Please enter the Acceration of the object')
                acceration = float(input())
    else:
        mass = random.randrange(2.99,150)
        acceration = random.randrange(2.5,28)
    ## Calculate force applied to the object   
    appliedForce = mass * acceration
    print(f'Given the Mass {mass} and Acceration {acceration} the force applied to the object is {appliedForce}')

    ## Prompt user to continue or terminate the loop
    print('Would you like to calculate the force applied to another object? \nEnter Yes/Y continue or No/n/Quit/Q to exit')
    optionMR = str(input()).upper()
    if optionMR in ['NO','N']:
        print('Thanks bye!! :)')
        calculateForce = False