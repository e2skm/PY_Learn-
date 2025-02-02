# Modules 101 - Using user-defined module String_utils-PY_learn_projectn
## Import user-defined module String_utils
import string_utils as strut

## Prompt user for a string
print('Please enter a word, phrase or sentence')
string = input()

## Get vowels and consonants from string
vowels, consonants = strut.count_vowels_and_consonants(string)
print(f'From the string {string}, there are {len(vowels)} vowels namely {vowels} and {len(consonants)} consonants namely {consonants}.')

## Get reverse string
reversedStr = strut.reverse_string(string)
print(f'The reversed version of {string} is {reversedStr}')

## Check if a word is a palindrome
strut.is_palindrome(string)

## Get the breakdown of a string
strut.partition(string)
