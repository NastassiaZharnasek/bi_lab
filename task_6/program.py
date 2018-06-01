import re


def is_palindrome(string):
    string = string.lower()
    string = re.sub("[^a-z]", "", string)
    inverse_str = string[::-1]
    print("Inverse string: " + inverse_str)
    if string == inverse_str:
        response = 'Palindrome'
    else:
        response = 'Not a palindrome'
    return response
