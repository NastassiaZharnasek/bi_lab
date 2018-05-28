import pytasks as py


def runner(args):
    if args:
        for i in args:
            getattr(py, i)()
    else:
        getattr(py, 'generate_numbers')()
        getattr(py, 'count_characters')()
        getattr(py, 'fizzbuzz')()
        getattr(py, 'happy_numbers')()
        getattr(py, 'is_palindrome')()
    return


runner(['generate_numbers', 'count_characters', 'happy_numbers'])
