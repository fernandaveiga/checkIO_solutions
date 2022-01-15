
def sum_by_types(list):
  sum_int = 0
  sum_str = ''
  for c in list:
    if type(c)== int:
      sum_int = sum_int + c
    elif type(c)==str:
      sum_str = sum_str + c
    else:
      pass
  return sum_str, sum_int

print(sum_by_types([]))
print(sum_by_types([1, 2, 3]))
print(sum_by_types(["1", 2, 3]))
print(sum_by_types(["1", "2", 3]))
print(sum_by_types(["1", "2", "3"]))