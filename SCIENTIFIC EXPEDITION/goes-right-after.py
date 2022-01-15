
def goes_after(string, a, b):
  if a in string and b in string:
    a1 = string.find(a)
    b1 = string.find(b)
    if a1+1 == b1:
      return True
    else:
      return False
  else:
    return False

print(goes_after('world', 'w', 'o'))
print(goes_after('world', 'w', 'r'))
print(goes_after('world', 'l', 'o'))
print(goes_after('panorama', 'a', 'n'))
print(goes_after('list', 'l', 'o'))
print(goes_after('list', 'l', 'l'))
print(goes_after('world', 'd', 'w'))
print(goes_after('almaz', 'r', 'a'))