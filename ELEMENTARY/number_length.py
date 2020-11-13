def number_length(int):
    '''You have a positive integer. Try to find out how many digits it has?

Input: A positive Int

Output: An Int.'''

    num = len(str(int))
    return num


if __name__ == '__main__':
    print("Example:")
    print(number_length(1009))
