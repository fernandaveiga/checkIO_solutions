def from_camel_case(string):
  frase = ''
  lista = []
  for pos, item in enumerate(string):
    if item.isupper():
      lista.append('_'+item)
    else:
      lista.append(item)
  lista = ''.join(lista).lower()
  if lista[0]=='_':
    lista = lista[1:]
  return lista


print(from_camel_case("MyFunctionName"))
print(from_camel_case("IPhone"))
print(from_camel_case("ThisFunctionIsEmpty"))
print(from_camel_case("Name"))
