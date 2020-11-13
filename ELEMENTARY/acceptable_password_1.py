def is_acceptable_password(str):
    '''
    You are at the beginning of a password series. Every mission is based on the previous one. Going forward the missions will become slightly more complex.

In this mission, you need to create a password verification function.

The verification condition is:

the length should be bigger than 6.
Input: A string.

Output: A bool.'''
    if len(str)>6:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

