
def common_words(str1, str2):
  lista = []
  str1 = str1.replace(',', ' ')
  str2 = str2.replace(',', ' ')
  str1 = str1.split()
  str2 = str2.split()
  for c in str1:
    if c in str2:
      lista.append(c)
    else:
      pass
  lista = sorted(lista)
  lista = ','.join(lista)

  return lista

print(common_words('hello,world', 'hello,earth'))
print(common_words('one,two,three', 'four,five,six'))
print(common_words('one,two,three',
 'four,five,one,two,six,three'))