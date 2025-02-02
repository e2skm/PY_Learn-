# Modules 101 - Create a module String_utils -PY_learn_projectn
## Function to divide a string into vowels and consonants
def count_vowels_and_consonants(string):
    vowels, consonants = '',''
    for c in string:  
        if c.isalpha():
            if c in 'aeiouAEIOU':  
                vowels += c
            else:
                consonants += c
    return vowels,consonants  
      
## Function two reverse the order of characters in a string
def reverse_string(string):
    newStr = string[::-1]
    return newStr 
     
## Function to check if a string is a palindrome
def is_palindrome(string):
    if reverse_string(string) == string:
        print(f'The string {string} is a palindrome as it reads the same in both directions.')
    else:
        print(f'The word {string} is not a palindrome as it results to {reverse_string(string)} when read backwards')  

## Function to breakdown a string 
def partition(string):
    alphabets, numbers, specialChars, spaces = '', '', '', ''
    alphaIndex, numIndex, specCharIndex, spaceIndex = [], [], [], []
    
    for i, c in enumerate(string):
        if c.isalpha():
            alphabets += c
            alphaIndex.append(i) 
        elif c.isdigit():
            numbers += c
            numIndex.append(i) 
        elif c.isspace():
            spaces += c
            spaceIndex.append(i)  
        else:
            specialChars += c 
            specCharIndex.append(i) 
            
    print(f'''The string {string} contains the following:\n-{len(alphabets)} alphabets @ indices {alphaIndex} namely: {alphabets}.\
          \n-{len(numbers)} numbers @ indices {numIndex} namely: {numbers}.\n-{len(spaces)} spaces @ indices {spaceIndex} namely: {spaces}.\
          \n-{len(specialChars)} special characters @ indices {specialChars} namely: {specialChars}.''')
                        
                       
                       
                  