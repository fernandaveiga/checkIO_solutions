lista1 = []
def max_digit(inteiro):
    '''
    You have a number and you need to determine which digit in this number is the biggest.

Input: A positive int.

Output: An Int (0-9).
    '''
    lista1.clear()
    for c in str(inteiro):
        lista1.append(int(c))
    return max(lista1)
    

if __name__ == '__main__':
    print("Example:")
    print(max_digit(181))
    print(max_digit(19375))
    print(max_digit(0))