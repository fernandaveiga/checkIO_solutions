def first_word(str):
    """
        returns the first word in a given text.
    """
    text=str.split()
    return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
