#One of the robots is charged with a simple task: to join a sequence of strings into one sentence to produce 
#instructions on how to get around the ship. But this robot is left-handed and has a tendency to joke around 
#and confuse its right-handed friends.
#You are given a sequence of strings. You should join these strings into a chunk of text where the initial 
#strings are separated by commas. As a joke on the right handed robots, you should replace all cases of 
#the words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.

def left_join(phrase):
    lista =[]
    for c in phrase:
        c=c.lower()
        lista.append(c)
    lista = ','.join(lista)
    return lista.replace('right', 'left')
    

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))
    print(left_join(("Left", "right", "left", "stop")))
    print(left_join(("bright aright", "ok")))
    print(left_join(("brightness wright",)))
    print(left_join(("enough", "jokes")))
