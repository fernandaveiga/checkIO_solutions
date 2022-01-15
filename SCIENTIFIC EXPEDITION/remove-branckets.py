
def remove_brackets(string):
  lista = []
  for pos,item in enumerate(string):
    if (item=='(') and (')' in string):
      if pos<string.find(')'):
        lista.append(item)
        lista.append(')')
    if (item=='[') and (']' in string):
      if pos<string.find(']'):
        lista.append(item)
        lista.append(']')
    if (item=='{') and ('}' in string):
      if pos<string.find('}'):
        lista.append(item)
        lista.append('}')
  lista = ''.join(lista)
  return lista