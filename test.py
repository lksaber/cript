import sys
import string
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
rota = 13



def encrypt(message):
    m = ''
    for c in message:
        c_index = ALPHABET.index(c)
        m += ALPHABET[(c_index + rota) % len(ALPHABET) ]
    return m


def decrypt(message):
    m = ''
    for c in message:
        c_index = ALPHABET.index(c)
        m += ALPHABET[(c_index - rota) % len(ALPHABET) ]
    return m



'''

message = input("algo")

message = cipher(message)
'''

def main():
    command = input('comando: ')
    message = input('mensagem: ')

    if command == 'encrypt':
          print (encrypt(message))
    elif command == 'decrypt':
          print (decrypt(message))     
    else:
        print ('commando não encontrado')

if __name__ == '__main__':
    main()

