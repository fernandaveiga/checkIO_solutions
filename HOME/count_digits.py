# You need to count the number of digits in a given string.

def count_digits(text):
    lista=[]
    lista.clear()
    for c in text:
        lista.append(c)
    count=0
    for c in lista:
        if c.isnumeric():
            count=count+1
    return count


if __name__ == '__main__':
    print("Example:")
    print(count_digits('hi'))
    print(count_digits('who is 1st here'))
    print(count_digits('my numbers is 2'))
    print(count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year'))
    print(count_digits('5 plus 6 is'))