# For the input of your function will be given one sentence.
# You have to return its fixed copy in a way so
# it’s always starts with a capital letter and ends with a dot.
# Pay attention to the fact that not all of the fixes is necessary.
# If a sentence already ends with a dot - adding another one will be a mistake.
# No leading and trailing spaces, text contains only spaces, a-z A-Z , and .


# This is script for this task but without using functions
# you may uncomment it and run

# text = input("Input: ")
# text = text[0].upper() + text[1:].lower()
# if text[len(text)-1] != '.':
#     text = text + '.'
# print(text)


def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:].lower()
    if text[-1] != '.':
        text = text + '.'
    return text


if __name__ == '__main__':
    print(correct_sentence("greetings, friends"))

    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
