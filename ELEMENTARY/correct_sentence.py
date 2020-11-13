def correct_sentence(text):
    '''
    For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.

Input: A string.

Output: A string.

Precondition: No leading and trailing spaces, text contains only spaces, a-z A-Z , and .
    '''
    text = text.strip()
    if text[-1]!='.':
        text=text+'.'
    text = text.split()
    text[0] =text[0].capitalize()
    text = ' '.join(text)
    #text = text.replace(text[0], text[0].upper())
    return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    print(correct_sentence("Greetings, friends"))
    print(correct_sentence("Greetings, friends."))
    print(correct_sentence("  hi    "))
    print(correct_sentence("welcome to New York"))