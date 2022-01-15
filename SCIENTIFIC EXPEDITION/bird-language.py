
def translate(string):
  string = list(string)
  for pos, item in enumerate(string):
    if item in 'bcdfghjklmnpqrstvwxz':
      del string[pos+1]
    elif item in 'aeiouy':
      if string[pos]==string[pos+1]==string[pos+2]:
        del string[pos:pos+2]
      else:
        pass
    else:
      pass
  string = ''.join(string)


  return string

print(translate('hieeelalaooo'))
print(translate('hoooowe yyyooouuu duoooiiine'))
print(translate('aaa bo cy da eee fe'))
print(translate('sooooso aaaaaaaaa'))