import re

# Write a program to find all email addresses in string
pattern = re.compile(r'\w+@\w+\.+\w+')
all_emails = pattern.findall('1email@test.com not email email@test.com')
print(all_emails)

# Write a program to find all three,four,five characters long words in a string
pattern = re.compile(r'\b\w{3,5}\b')
all_words = pattern.findall('this is test for task 2. Extraordinary long word')
print(all_words)

# Write a program to separate and print the numbers of a given string.
pattern = re.compile(r'\d+')
all_numbers = pattern.findall('this is test for task 3. 44 88 9912test34')
print(all_numbers)

# to replace whitespaces with an underscore and vice versa
test_string = 'This is test string for task_4'
test_string_with_underscores = test_string.replace(' ', '_')
test_string_with_whitespaces = test_string.replace('_', ' ')
print(test_string_with_underscores)
print(test_string_with_whitespaces)

