def is_all_upper(str):
    '''
    Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.

Output: a boolean.

Precondition: a-z, A-Z, 1-9 and spaces
    '''
    if str== str.upper():
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))
    print(is_all_upper('All upper'))
    print(is_all_upper('all upper'))