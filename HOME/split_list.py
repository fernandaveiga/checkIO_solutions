#You have to split a given array into two arrays. If it has an odd amount of elements, then the first array 
#should have more elements. If it has no elements, then two empty arrays should be returned.

def split_list(items):
    lista3 = []
    if len(items)%2==0:
        metade = int(len(items)/2)
        lista3.clear()
        lista3.append(items[0:metade])
        lista3.append(items[metade:])
    else:
        metade = int((len(items)//2)+1)
        lista3.append(items[0:metade])
        lista3.append(items[metade:])
    return lista3


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))
    print(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
    print(split_list([1, 2, 3])) == [[1, 2], [3]]
    print(split_list([1, 2, 3, 4, 5])) == [[1, 2, 3], [4, 5]]
    print(split_list([1])) == [[1], []]
    print(split_list([])) == [[], []]