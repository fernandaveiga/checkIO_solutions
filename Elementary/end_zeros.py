def end_zeros(int):
    '''
    Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.
    '''
    d=0
    if int>=10:     
        while int%10==0:
            d=d+1
            int=int/10
    elif int==0:
        d=1
    else:
        d=0
    return d


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(101000))
    print(end_zeros(100000))
    print(end_zeros(100010))
    print(end_zeros(0))
    print(end_zeros(1))