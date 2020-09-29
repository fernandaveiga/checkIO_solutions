def between_markers(text,mark1,mark2):
    '''
    You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

This is a simplified version of the Between Markers mission.

The initial and final markers are always different.
The initial and final markers are always 1 char size.
The initial and final markers always exist in a string and go one after another.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Precondition: There can't be more than one final and one initial markers.
    '''
    if mark1 and mark2 in text:
        i1 = text.index(mark1)
        i2 = text.index(mark2)
        if i1<i2:
            return text[text.index(mark1)+1:text.index(mark2)]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    print(between_markers('What is [apple]', '[', ']'))
    print(between_markers('What is ><', '>', '<'))
    print(between_markers('>apple<', '>', '<'))
    print(between_markers('an -apologize> to read', '-', '>'))
