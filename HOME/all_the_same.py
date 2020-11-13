#In this mission you should check if all elements in the given list are equal.

from typing import List, Any
def all_the_same(elements):
    if len(elements)==0:
        return True
    else:
        if len(set(elements))==1:
            return True
        else:
            return False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1])) == True
    print(all_the_same([1, 2, 1])) == False
    print(all_the_same(['a', 'a', 'a'])) == True
    print(all_the_same([])) == True
    print(all_the_same([1])) == True