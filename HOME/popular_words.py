#In this mission your task is to determine the popularity of certain words in the text.
#At the input of your function are given 2 arguments: the text and the array of words the 
#popularity of which you need to determine.
#When solving this task pay attention to the following points:
#The words should be sought in all registers. This means that if you need to find a word 
#"one" then words like "one", "One", "oNe", "ONE" etc. will do.
#The search words are always indicated in the lowercase.
#If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.

def popular_words(text, words):
    dicio = {}
    lista = []
    text = text.lower()
    text = text.split()
    for c in words:
      for pos,item in enumerate(words):
        if c==item:
          d=text.count(c)
      lista.append(d)
    for pos, item in enumerate(words):
        dicio[item]=lista[pos]
    return dicio
    
if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))