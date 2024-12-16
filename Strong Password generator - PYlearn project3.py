# Strong Password generator - PYlearn project3
## Import the necessary liabraries
import secrets, string
## Define a method to generate a password
def generate_password(length=12):
    alphabet = (string.ascii_letters + string.digits + string.punctuation)
    return ''.join(secrets.choice(alphabet) for _ in range(length))
password = generate_password()
print(f'Your password is: {password}')
## Define a method to check if the password generated is a strong password
def is_strong_password(password):
    isStrongPassword = False
    passInfo = ""
    hasUppercase,hasLowercase,hasDigits,hasSpecialChar = 0,0,0,0
    for p in range(len(password)):
        character = password[p]
        if character.isupper():
            hasUppercase += 1
        elif character.islower():
            hasLowercase += 1
        elif character.isdigit():
            hasDigits += 1
        else:
            hasSpecialChar += 1
    passInfo = 'It contains: {0} Uppercase {1} Lowercase {2} Digits {3} Special characters'.format({hasUppercase},{hasLowercase},{hasDigits},{hasSpecialChar})

    if hasDigits >= 1:
        hasDigits = True
    if hasLowercase >= 1:
        hasLowercase = True
    if hasUppercase >= 1:
        hasUppercase = True
    if hasSpecialChar >= 1:
        hasSpecialChar = True
    
    
    if hasDigits is True and hasLowercase is True and hasUppercase is True and hasSpecialChar is True:
        isStrongPassword = True
        print('The generated password is Strong')
        print(passInfo)            
    else:
        print('The generated password is weak')
        print(passInfo)
        if hasUppercase == 0:
            print('There are no Uppercase characters in the generated password')
        elif hasLowercase == 0:
            print('There are no Lowercase characters in the generated password')
        elif hasDigits == 0:
            print('There are no Digits in the generated password')
        else:
            print('There are no Special characters in the generated password')
    return is_strong_password
checkPassword = is_strong_password(password)