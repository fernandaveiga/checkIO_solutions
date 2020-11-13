#In a given text you need to sum the numbers. Only separated numbers should be counted. If a number is part of a word it shouldn't be counted.

#The text consists from numbers, spaces and english letters

def sum_numbers(str):
    soma=0
    for c in str.split():
        if c.isdigit():
            soma=soma+int(c)
    return soma


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi 99 99'))