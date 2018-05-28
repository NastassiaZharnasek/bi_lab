import re


def generate_numbers(number=20):
    dictionary1 = {}
    for i in range(1, number + 1):
        dictionary1[i] = i * i
    print(dictionary1)
    return [dictionary1]


def count_characters(count_me_string='tghatth'):
    dictionary2 = {}
    for i in count_me_string:
        dictionary2[i] = dictionary2.get(i, 0) + 1
    print(dictionary2)
    return [dictionary2]


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
            continue
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
            continue
        else:
            print(i)


def happy_numbers(number=19):
    visited = set()
    while 1:
        if number == 1:
            print("Number is happy:)")
            break
        number = sum(int(i) ** 2 for i in str(number))
        if number in visited:
            print("Number is not happy:(")
            break
        visited.add(number)


def is_palindrome():
    string = 'edcvbvcde'.lower()
    string = re.sub("[^a-z]", "", string)
    inverse_str = string[::-1]
    print("Inverse string: " + inverse_str)
    if string == inverse_str:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")
