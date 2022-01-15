def checkio(string):
  dicio = {}
  lista = []
  string = string.lower()
  string = sorted(string, reverse = True)
  for pos, item in enumerate(string):
    if item in 'abcdefghijklmnopqrstuvwxyz':
      count = string.count(item)
      dicio[count] = item
      lista.append(count)
    else:
      pass
  maximo = max(lista)
  return dicio[maximo]

print(checkio("Hello World!"))
print(checkio("How do you do?"))
print(checkio("One"))
print(checkio("Oops!"))
print(checkio("AAaooo!!!!"))
print(checkio("abe"))