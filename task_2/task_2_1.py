import re

string = str(input("Input string: ")).lower()
string = re.sub("[^a-z]", "", string)
inverse_str = string[::-1]
print("Inverse string: " + inverse_str)
if string == inverse_str:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
