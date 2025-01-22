# Units Interpretor - PY_Learn_projectn
## Function to get conversion direction
def conversion_direction():
    while True:
        try:
            print('Please enter any of the options given below:\n- Enter 1 to convert from Imperial to Metric units.\n- Enter 2 to convert from Metric to Imperial')
            conDire = int(input())
            if conDire in [1,2]:
                break
        except Exception:
            print('Error!! Carefully read the followint instruction')   
    return conDire        

## Function to get number of conversions
def num_of_conversions():
    while True:
        try:
            print('Please enter any of the options given below:\n- Enter 1 to convert weight.\n- Enter 2 to convert height.\n- Enter 3 to convert both weight and height.')
            numConv = int(input())
            if numConv in [1,2,3]:
                break
        except Exception:
            print('Error!! Carefully read the following instruction')         
    return numConv

## Function to get weight
def get_weight(conDire):
    if conDire == 1:
        while True:
            try:
                print('Enter your weight in Pounds (lbs)')
                weight = float(input())
                break 
            except Exception: 
                 print('Error!! Carefully follow the instructions below')
    else:
        while True:
            try:
                print('Enter your weight in Kilograms (kg)')
                weight = float(input())
                break               
            except Exception: 
                 print('Error!! Carefully follow the instructions below')              
    return weight

## Function to get height 
def get_height(conDire):
    if conDire == 1:
        while True:
            try:
                print('Enter your height in Inces (In)')
                height = float(input())
                break 
            
            except Exception: 
                 print('Error!! Carefully follow the instructions below')
    else:
        while True:
            try:
                print('Enter your height in Centimeters (cm)')
                height = float(input())
                break               
            except Exception: 
                 print('Error!! Carefully follow the instructions below')                
    return height
     

## Functions to perform conversion(s)
### Function to convert weight
def convert_weight(conDire,weight):
    if conDire == 1:
        weightConverted = round(weight / 2.205, 2) 
        print(f'The weight of {weight} lbs is equal to {weightConverted} kg')
    else:
        weightConverted = round(weight * 2.205,2)
        print(f'The weight of {weight} kg is equal to {weightConverted} lbs') 
                     
### Function to convert height
def convert_height(conDire,height):
    if conDire == 1:
        heightConverted = round(height * 2.54, 2) 
        print(f'The height of {height} ln is equal to {heightConverted} cm')
    else:
        heightConverted = round(height / 2.54, 2) 
        print(f'The height of {height} cm is equal to {heightConverted} ln') 

## Function to get stop 
def get_stop():
    while True:
        try:
            print('Would you like to perform another conversion ?\n- Enter "Yes/Y" to Proceed.\n- Enter "No/N" to Stop.')
            stop = input().upper()
            if stop in ["N0", "N","Yes","Y"]:
                break
        except Exception: 
            print('Error!! Carefully follow the instructions below')  
    return stop                         
        
## Main program function
def main():
    while True:
        conDire = conversion_direction()
        numConv = num_of_conversions()
        if numConv == 1: 
            weight = get_weight(conDire)
            convert_weight(conDire,weight)
        elif numConv == 2: 
            height = get_height(conDire)
            convert_height(conDire,height)
        else:
            weight = get_weight(conDire)
            height = get_height(conDire)
            convert_weight(conDire,weight)
            convert_height(conDire,height)    
        ### 
        stop = get_stop()
        if stop in ["N0", "N"]:
            print('Thanks bye :)')
            break

main()                          