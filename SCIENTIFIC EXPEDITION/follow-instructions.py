def follow(string):
  string=list(string)
  countf = string.count('f')
  countb = string.count('b')
  countl = string.count('l')
  countr = string.count('r')
  countx = countr-countl
  county = countf-countb

  return (countx, county)

print(follow('fflff'))
print(follow('ffrff'))
print(follow('fblr'))