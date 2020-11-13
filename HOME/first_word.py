#You are given a string where you have to find its first word.
#When solving a task pay attention to the following points:
#There can be dots and commas in a string.
#A string can start with a letter or, for example, a dot or space.
#A word can contain an apostrophe and it's a part of a word.
#The whole text can be represented with one word and that's it.

def first_word(text):
    text = text.replace('.', ' ').replace(',',' ')
    text = text.strip()
    text = text.split()
    for c in text[0]:
        if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    print(first_word(" a word "))
    print(first_word("don't touch it"))
    print(first_word("greetings, friends"))
    print(first_word("... and so on ..."))
    print(first_word("hi"))
    print(first_word("Hello.World"))