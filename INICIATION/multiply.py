def mult_two(a, b):
    mult = a*b
    return mult


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))
    assert mult_two(3, 2)
    assert mult_two(1, 0)
