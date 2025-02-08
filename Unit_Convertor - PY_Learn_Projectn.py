# Unit_Convertor - PY_Learn_Projectn
## Function to get the unit for the conversion
def get_unit():
    while True:
        try:
            print('Please enter any of the options provided below:\n- V to convert Volume.\n- M to convert Mass.\n- L to convert Length.\n- T to convert Temperature.')
            convertUnit = input().upper()
            if convertUnit in ['V', 'VOLUME', 'M', 'MASS', 'L', 'LENGTH', 'T', 'TEMPERATURE']:
                break
        except Exception:
            print('Error!! kindly follow these instructions')
    return convertUnit

## Function to get conversion direction
def get_measurements():
    while True:
        try:
            print('''Please enter any of the options provided below:\n- 1 to convert a Metric unit to Imperial unit.\n- 2 to convert an Imperial unit to Metric unit.''')
            unitMeas = int(input())
            if unitMeas in [1, 2]:
                break
        except Exception:
            print('Error!! kindly follow these instructions')
    return unitMeas

## Function to get the unit quantity
def get_quant():
    while True:
        try:
            print('Please enter the quantity you want to convert')
            quantity = float(input())
            break
        except Exception:
            print('Error!! kindly follow these instructions')
    return quantity

## Function to get specific measure of quantity
def quantity_measure(convertUnit, unitMeas):
    if convertUnit in ['V', 'VOLUME']:
        while True:
            try:
                if unitMeas == 1:
                    print('''Please enter any of the options provided below:\n- ml to convert milliliters.\
                          \n- l if your value is in liters.\n- kl if your value is in kiloliters.''')
                    quantMeas = input().lower()
                    if quantMeas in ['ml', 'l', 'kl']:
                        break
                else:
                    print('''Please enter any of the options provided below:\n- oz to convert fluid ounces.\
                       \n- pt if your value is in pints.\n- qt if your value is in quarts.\n- gal if your value is in gallons.''')
                    quantMeas = input().lower()
                    if quantMeas in ['oz', 'pt', 'qt', 'gal']:
                        break
            except Exception:
                print('Error!! kindly follow these instructions')
    elif convertUnit in ['M', 'MASS']:
        while True:
            try:
                if unitMeas == 1:
                    print('''Please enter any of the options provided below:\n- g to convert grams.\n- kg if your value is in kilograms.''')
                    quantMeas = input().lower()
                    if quantMeas in ['g', 'kg']:
                        break
                else:
                    print('''Please enter any of the options provided below:\n- oz to convert ounces.\
                          \n- lb if your value is in pounds.\n- ton if your value is in short tons.''')
                    quantMeas = input().lower()
                    if quantMeas in ['oz', 'lb', 'ton']:
                        break
            except Exception:
                print('Error!! kindly follow these instructions')
    elif convertUnit in ['L', 'LENGTH']:
        while True:
            try:
                if unitMeas == 1:
                    print('''Please enter any of the options provided below:\n- mm to convert millimeters.\
                       \n- cm if your value is in centimeters.\n- m if your value is in meters.\n- km if your value is in kilometers.''')
                    quantMeas = input().lower()
                    if quantMeas in ['mm', 'cm', 'm', 'km']:
                        break
                else:
                    print('''Please enter any of the options provided below:\n- in to convert inches.\
                       \n- ft if your value is in feet.\n- y if your value is in yards.\n- mi if your value is in miles.''')
                    quantMeas = input().lower()
                    if quantMeas in ['in', 'ft', 'y', 'mi']:
                        break
            except Exception:
                print('Error!! kindly follow these instructions')
    elif convertUnit in ['T', 'TEMPERATURE']:
        while True:
            try:
                if unitMeas == 1:
                    print('''Please enter any of the options provided below:\n- C to convert Celsius.''')
                    quantMeas = input().upper()
                    if quantMeas == 'C':
                        break
                else:
                    print('''Please enter any of the options provided below:\n- F to convert Fahrenheit.''')
                    quantMeas = input().upper()
                    if quantMeas == 'F':
                        break
            except Exception:
                print('Error!! kindly follow these instructions')
    return quantMeas

## Function to convert the unit as specified
def convert_quantity(unitMeas, convertUnit, quantMeas, quantity):
    if convertUnit in ['V', 'VOLUME']:
        if unitMeas == 1:
            if quantMeas == 'ml':
                fl_oz = quantity * 0.033814
                pt = quantity * 0.00211338
                qt = quantity * 0.00105669
                gal = quantity * 0.000264172
                print(f'{quantity} milliliters is equal to {fl_oz:.2f} fluid ounces, {pt:.2f} pints, {qt:.2f} quarts, and {gal:.2f} gallons.')
            elif quantMeas == 'l':
                fl_oz = quantity * 33.814
                pt = quantity * 2.11338
                qt = quantity * 1.05669
                gal = quantity * 0.264172
                print(f'{quantity} liters is equal to {fl_oz:.2f} fluid ounces, {pt:.2f} pints, {qt:.2f} quarts, and {gal:.2f} gallons.')
            elif quantMeas == 'kl':
                fl_oz = quantity * 33814
                pt = quantity * 2113.38
                qt = quantity * 1056.69
                gal = quantity * 264.172
                print(f'{quantity} kiloliters is equal to {fl_oz:.2f} fluid ounces, {pt:.2f} pints, {qt:.2f} quarts, and {gal:.2f} gallons.')
        else:
            if quantMeas == 'oz':
                ml = quantity * 29.5735
                l = quantity * 0.0295735
                kl = quantity * 0.0000295735
                print(f'{quantity} fluid ounces is equal to {ml:.2f} milliliters, {l:.2f} liters, and {kl:.2f} kiloliters.')
            elif quantMeas == 'pt':
                ml = quantity * 473.176
                l = quantity * 0.473176
                kl = quantity * 0.000473176
                print(f'{quantity} pints is equal to {ml:.2f} milliliters, {l:.2f} liters, and {kl:.2f} kiloliters.')
            elif quantMeas == 'qt':
                ml = quantity * 946.353
                l = quantity * 0.946353
                kl = quantity * 0.000946353
                print(f'{quantity} quarts is equal to {ml:.2f} milliliters, {l:.2f} liters, and {kl:.2f} kiloliters.')
            elif quantMeas == 'gal':
                ml = quantity * 3785.41
                l = quantity * 3.78541
                kl = quantity * 0.00378541
                print(f'{quantity} gallons is equal to {ml:.2f} milliliters, {l:.2f} liters, and {kl:.2f} kiloliters.')

    elif convertUnit in ['M', 'MASS']:
        if unitMeas == 1:
            if quantMeas == 'g':
                oz = quantity * 0.035274
                lb = quantity * 0.00220462
                ton = quantity * 0.00000110231
                print(f'{quantity} grams is equal to {oz:.2f} ounces, {lb:.2f} pounds, and {ton:.2f} short tons.')
            elif quantMeas == 'kg':
                oz = quantity * 35.274
                lb = quantity * 2.20462
                ton = quantity * 0.00110231
                print(f'{quantity} kilograms is equal to {oz:.2f} ounces, {lb:.2f} pounds, and {ton:.2f} short tons.')
        else:
            if quantMeas == 'oz':
                g = quantity * 28.3495
                kg = quantity * 0.0283495
                print(f'{quantity} ounces is equal to {g:.2f} grams and {kg:.2f} kilograms.')
            elif quantMeas == 'lb':
                g = quantity * 453.592
                kg = quantity * 0.453592
                print(f'{quantity} pounds is equal to {g:.2f} grams and {kg:.2f} kilograms.')
            elif quantMeas == 'ton':
                g = quantity * 907185
                kg = quantity * 907.185
                print(f'{quantity} short tons is equal to {g:.2f} grams and {kg:.2f} kilograms.')

    elif convertUnit in ['L', 'LENGTH']:
        if unitMeas == 1:
            if quantMeas == 'mm':
                in_ = quantity * 0.0393701
                ft = quantity * 0.00328084
                y = quantity * 0.00109361
                mi = quantity * 0.000000621371
                print(f'{quantity} millimeters is equal to {in_:.2f} inches, {ft:.2f} feet, {y:.2f} yards, and {mi:.2f} miles.')
            elif quantMeas == 'cm':
                in_ = quantity * 0.393701
                ft = quantity * 0.0328084
                y = quantity * 0.0109361
                mi = quantity * 0.00000621371
                print(f'{quantity} centimeters is equal to {in_:.2f} inches, {ft:.2f} feet, {y:.2f} yards, and {mi:.2f} miles.')
            elif quantMeas == 'm':
                in_ = quantity * 39.3701
                ft = quantity * 3.28084
                y = quantity * 1.09361
                mi = quantity * 0.000621371
                print(f'{quantity} meters is equal to {in_:.2f} inches, {ft:.2f} feet, {y:.2f} yards, and {mi:.2f} miles.')
            elif quantMeas == 'km':
                in_ = quantity * 39370.1
                ft = quantity * 3280.84
                y = quantity * 1093.61
                mi = quantity * 0.621371
                print(f'{quantity} kilometers is equal to {in_:.2f} inches, {ft:.2f} feet, {y:.2f} yards, and {mi:.2f} miles.')
        else:
            if quantMeas == 'in':
                mm = quantity * 25.4
                cm = quantity * 2.54
                m = quantity * 0.0254
                km = quantity * 0.0000254
                print(f'{quantity} inches is equal to {mm:.2f} millimeters, {cm:.2f} centimeters, {m:.2f} meters, and {km:.2f} kilometers.')
            elif quantMeas == 'ft':
                mm = quantity * 304.8
                cm = quantity * 30.48
                m = quantity * 0.3048
                km = quantity * 0.0003048
                print(f'{quantity} feet is equal to {mm:.2f} millimeters, {cm:.2f} centimeters, {m:.2f} meters, and {km:.2f} kilometers.')
            elif quantMeas == 'y':
                mm = quantity * 914.4
                cm = quantity * 91.44
                m = quantity * 0.9144
                km = quantity * 0.0009144
                print(f'{quantity} yards is equal to {mm:.2f} millimeters, {cm:.2f} centimeters, {m:.2f} meters, and {km:.2f} kilometers.')
            elif quantMeas == 'mi':
                mm = quantity * 1609344
                cm = quantity * 160934.4
                m = quantity * 1609.344
                km = quantity * 1.609344
                print(f'{quantity} miles is equal to {mm:.2f} millimeters, {cm:.2f} centimeters, {m:.2f} meters, and {km:.2f} kilometers.')

    elif convertUnit in ['T', 'TEMPERATURE']:
        if unitMeas == 1:
            if quantMeas == 'C':
                f = (quantity * 9/5) + 32
                print(f'{quantity} degrees Celsius is equal to {f:.2f} degrees Fahrenheit.')
        else:
            if quantMeas == 'F':
                c = (quantity - 32) * 5/9
                
                print(f'{quantity} degrees Fahrenheit is equal to {c:.2f} degrees Celsius.')

## Main function to run the program
def main():
    convertUnit = get_unit()
    unitMeas = get_measurements()
    quantity = get_quant()
    quantMeas = quantity_measure(convertUnit, unitMeas)
    convert_quantity(unitMeas, convertUnit, quantMeas, quantity)

if __name__ == "__main__":
    main()