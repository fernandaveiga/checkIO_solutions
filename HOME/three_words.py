#Let's teach the Robots to distinguish words and numbers.
#You are given a string with words and numbers separated by whitespaces (one space). 
#The words contains only letters. You should check if the string contains three words in succession. 
#For example, the string "start 5 one two three 7 end" contains three words in succession.

def checkio(string):
    string = string.split()
    lista = []
    for c in string:
        if c.isalpha():
            lista.append(c)
            if len(lista)==3:
                break
        else:
            lista.clear()
    if len(lista)==3:
        return True
    else:
        return False

if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    print(checkio("haaas h366lo hello"))
    print(checkio('o 111 rato roeu a  111roupa do rei de roma'))
    print(checkio('he is 123 man'))
    print(checkio('one two 3 four five six 7 eight 9 ten eleven 12'))