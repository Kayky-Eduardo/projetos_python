import os


os.system('cls')

frase = input('Digite uma frase: ')

vogais = frase.count('a', 'e', 'i', 'o', 'u')

print(f'O número de vezes que aparece as vogais são {vogais}')