#You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...). 
#Then multiply this summed number and the final element of the array together.
#Don't forget that the first element has an index of 0.
#For an empty array, the result will always be 0 (zero).

def checkio(list):
    """
        sums even-indexes elements and multiply at the last
    """
    soma=0
    if len(list)>0:
        for pos, item in enumerate(list):
            if pos%2==0:
                soma=soma+item
        mult=soma*list[-1]
        return mult
    else:
        return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([1, 1, 2, 3, 4, 5]))
    print(checkio([]))
    