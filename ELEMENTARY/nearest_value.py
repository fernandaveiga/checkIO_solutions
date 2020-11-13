def nearest_value(sett, num):
    '''
    Find the nearest value to the given one.

You are given a list of values as set form and a value for which you need to find the nearest one.

For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17, and we need to find the nearest value to the number 9. If we sort this set in the ascending order, then to the left of number 9 will be number 7 and to the right - will be number 10. But 10 is closer than 7, which means that the correct answer is 10.

A few clarifications:

If 2 numbers are at the same distance, you need to choose the smallest one;
The set of numbers is always non-empty, i.e. the size is >=1;
The given value can be in this set, which means that it’s the answer;
The set can contain both positive and negative numbers, but they are always integers;
The set isn’t sorted and consists of unique numbers.
Input: Two arguments. A list of values in the set form. The sought value is an int.

Output: Int.
    '''
    lista1 = []
    lista1.clear()
    for c in sett:
        lista1.append(c)
    lista1.append(num)
    lista1 = sorted(lista1)
    for pos, item in enumerate(lista1):
        if item==num:
            if num==lista1[0]:
                return lista1[1]
            if num==lista1[-1]:
                return lista1[-2]
            else:
                ante = lista1[pos]-lista1[pos-1]
                poste = lista1[pos+1]-lista1[pos]
                if ante<poste:
                    return lista1[pos-1]
                elif ante==poste:
                    return lista1[pos-1]
                else:
                    return lista1[pos+1]
                


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
    print(nearest_value({4, 7, 10, 11, 12, 17}, 8))
    print(nearest_value({4, 8, 10, 11, 12, 17}, 9))
    print(nearest_value({4, 9, 10, 11, 12, 17}, 9))
    print(nearest_value({4, 7, 10, 11, 12, 17}, 0))
    print(nearest_value({4, 7, 10, 11, 12, 17}, 100))
    print(nearest_value({5, 10, 8, 12, 89, 100}, 7))
    print(nearest_value({-1, 2, 3}, 0))
