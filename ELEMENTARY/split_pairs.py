lista = []
def split_pairs(a):
    '''
    Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings.

Precondition: 0<=len(str)<=100
    '''
    lista.clear()
    for c in range(0, len(a), 2):
        if len(a)%2==0:
            lista.append(a[c:c+2])
        if len(a)%2==1:
            a = a+'_'
            lista.append(a[c:c+2])
    return lista


if __name__ == '__main__':
    print("Example:")
    print(split_pairs('abcd'))

    # These "asserts" are used for self-checking and not for an auto-testing
    print(split_pairs('abc'))
    print(split_pairs('abcdf'))
    print(split_pairs('a'))
    print(split_pairs(''))
