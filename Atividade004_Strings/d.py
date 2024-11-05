import os


os.system('cls')

frase = input('Digite uma frase: ')

minuscula = frase.lower()
maiuscula = frase.upper()
quantidade_de_caracteres = len(frase)

print(minuscula)
print(maiuscula)
print(quantidade_de_caracteres)

lista = frase.split(',')
print(f'{lista}')