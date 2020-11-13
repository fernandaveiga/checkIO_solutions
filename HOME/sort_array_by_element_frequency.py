#Sort the given iterable so that its elements end up in the decreasing frequency order, that is, 
#the number of times they appear in elements. If two elements have the same frequency, they should
# end up in the same order as the first appearance in the iterable.

from collections import Counter
def frequency_sort(items):
    c = Counter(items)
    lista = sorted(c.elements(), key=lambda k: c[k], reverse=True)
    return lista


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    print(frequency_sort([17, 99, 42])) == [17, 99, 42]
    print(frequency_sort([])) == []
    print(frequency_sort([1])) == [1]
