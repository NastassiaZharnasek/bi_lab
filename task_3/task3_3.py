# Define a function generate_numbers(number) which returns
# a dictionary where the keys are numbers between 1 and n (both included)
# and the values are square of keys. n – function argument. Default is 20


def generate_numbers(number=20):
    return {i: i*i for i in range(1, number + 1)}


print(generate_numbers(10))


# Define a function count_characters(count_me_string) which count and return
# the numbers of each character in a count_me_string argument.


def count_characters(count_me_string):
    dictionary2 = {}
    for i in count_me_string:
        dictionary2[i] = dictionary2.get(i, 0) + 1
    return [dictionary2]


print(count_characters('asdfada'))

