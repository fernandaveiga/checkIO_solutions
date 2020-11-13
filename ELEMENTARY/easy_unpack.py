tuple2 = ()
def easy_unpack(tuple):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    tuple2=(tuple[0], tuple[2], tuple[-2])
    return tuple2

if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))