#You are given a string and two markers (the initial and final). You have to find a substring enclosed between 
#these two markers. But there are a few important conditions:
#The initial and final markers are always different.
#If there is no initial marker, then the first character should be considered the beginning of a string.
#If there is no final marker, then the last character should be considered the ending of a string.
#If the initial and final markers are missing then simply return the whole string.
#If the final marker comes before the initial marker, then return an empty string.

def between_markers(string, initial, final):
  d=0
  e=0
  for c in initial:
    d=d+1
  for a in final:
    e=e+1
  antes = string.find(initial)
  depois = string.find(final)
  n1 = antes+d
  n2 = depois
  if initial!=final:
    if initial in string and final in string:
      if antes<depois:
        return string[n1:n2]
      else:
        return ''
    elif initial in string and final not in string:
      return string[n1:]
    elif initial not in string and final in string:
      return string[:n1]
    else:
      return string

        
if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    print(between_markers("<head><title>My new site</title></head>", "<title>", "</title>"))
    print(between_markers('No[/b] hi', '[b]', '[/b]'))
    print(between_markers('Nou [b]hi', '[b]', '[/b]'))
    print(between_markers('Noi hi', '[b]', '[/b]'))
    print(between_markers('Noe <hi>', '>', '<'))