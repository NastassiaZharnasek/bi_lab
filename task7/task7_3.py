# Write a function to compute 5/0 and use try/except to catch the
# DivisionError exception.
try:
    result = 5 / 0
except ZeroDivisionError:
    print('Division by zero!')


# Add a try-except statement to the body of this function which handles a
# possible IndexError, which could occur if the index provided exceeds the
# length of the list. Print an error message if this happens:
def print_list_element(the_list, index):
    try:
        print(the_list[index])
    except IndexError:
        print('Index of element exceeds the_list size!')


# This function adds an element to a list inside a dict of lists.
# Rewrite it to use a try-except statement which handles a possible KeyError
#  if the list with the name provided does not exist in the dictionary yet,
# instead of checking beforehand whether it does. Include else and
#  finally clauses in your try-except block:
def add_to_list_in_dict(the_dict, list_name, element):
    try:
        exist_list = the_dict[list_name]
        print("%s already has %d elements." % (list_name, len(exist_list)))
    except KeyError:
        the_dict[list_name] = []
        print("Created %s." % list_name)
    finally:
        the_dict[list_name].append(element)
        print("Added %s to %s." % (element, list_name))
