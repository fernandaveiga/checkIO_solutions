#Your task is to decrypt the secret message using the Morse code.
#The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
#If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

def morse_decoder(code):
    MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }


    string = ''
    code = code.split(' ')
    for c in code:
      if c in MORSE:
        string = string + MORSE[c]
      elif c=='' and string [-1]!= ' ':
        string = string + ' '
    string = string.capitalize()
    return string
        

if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))
    print(morse_decoder("... --- -- .   - . -..- -")) == "Some text"
    print(morse_decoder("..--- ----- .---- ---..")) == "2018"
    print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--")) == "It was a good day"
