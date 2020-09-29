def is_even(int):
    '''
    Check if the given number is even or not. Your function should return True if the number is even, and False if the number is odd.

Input: An int.

Output: A bool.

Precondition: both given ints should be between -1000 and 1000
    '''
    if int%2==0:
        return True
    if int%2==1:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))
    print(is_even(5))
    print(is_even(547))
    print(is_even(546))
