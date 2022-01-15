def find_message(string):
  lista = []
  for c in string:
    if c.isupper()==True:
      lista.append(c)
  lista = ''.join(lista)
  return lista

print(find_message(('How are you? Eh, ok. Low or Lower? '
 'Ohhh.')))
print(find_message('hello world!'))
print(find_message('HELLO WORLD!!!'))

