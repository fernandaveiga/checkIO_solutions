def beginning_zeros(string):
    '''
    You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int.

Precondition: 0-9
    '''
    count = 0
    lista = []
    lista2 = []
    lista.clear()
    lista =list(string)
    for c in lista:
        lista2.append(int(c))
    for c in lista2:
        if c==0:
            count=count+1
        if c!=0:
            break
    return count


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))
    print(beginning_zeros('001'))
    print(beginning_zeros('100100'))
    print(beginning_zeros('001001'))
    
