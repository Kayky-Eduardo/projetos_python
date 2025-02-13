import os


os.system('cls')

frase = input('Digite uma frase: ')

a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')
total = a + e + i + o + u

print(f'O número de vezes que aparece as vogais são {total}')