
def caps_lock(string):
  string= string.split('a')
  for pos, item in enumerate(string):
    if pos%2==1:
      string[pos] = string[pos].upper()
  string = ''.join(string)
  return string

print(caps_lock("Why are you asking me that?"))
print(caps_lock("Madder than Mad Brian of Madcastle"))
print(caps_lock("Aloha from Hawaii"))