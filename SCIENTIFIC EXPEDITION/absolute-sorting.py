def absolute_sorting(lista):
  lista = sorted(lista, key=lambda x: abs(x))
  return lista



print(absolute_sorting([-20, -5, 10, 15]))
print(absolute_sorting([1, 2, 3, 0]))
print(absolute_sorting([-1, -2, -3, 0]))