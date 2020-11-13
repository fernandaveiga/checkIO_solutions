# In a given string you should reverse every word, but the words should stay in their places.

def backward_string_by_word(text):
    lista = []
    text = text.split(' ')
    for c in text:
        c = c[::-1]
        lista.append(c)
    return ' '.join(lista)


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))
    print(backward_string_by_word('hello world'))
    print(backward_string_by_word('hello   world'))
    print(backward_string_by_word('welcome to a game'))