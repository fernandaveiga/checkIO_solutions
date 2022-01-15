def time_converter(string):
  string = string.split()
  hora = int(string[0][1])+(10*int(string[0][0]))
  if hora>=18:
    hora_pm = hora-12
    lista = [str(hora_pm), string[0][2], string[0][3], string[0][4], ' p.m.']
    lista = ''.join(lista)
    return lista
  else:
    if hora>=12:
      string.append(' p.m.')
      string = ''.join(string)
      return string
    else:
      if hora==0:
        lista = ['12', string[0][2], string[0][3], string[0][4], ' a.m.']
        string = ''.join(lista)
        return string
      elif hora<10 and hora!=0:
        string.append(' a.m.')
        string = ''.join(string)
        return string[1:]
      else:
        return string

print(time_converter('12:30'))
print(time_converter('09:00'))
print(time_converter('23:15'))
print(time_converter('00:30'))
print(time_converter('00:00'))