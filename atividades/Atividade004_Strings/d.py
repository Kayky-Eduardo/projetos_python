import os


os.system('cls')

frase = input('Digite uma frase: ')

minuscula = frase.lower()
maiuscula = frase.upper()
quantidade_de_caracteres = len(frase)

print(minuscula)
print(maiuscula)
print(quantidade_de_caracteres)

quebrada = frase.split()
quantidade_de_elementos = len(quebrada[1])
print(f'{quebrada}')
print(f'{quantidade_de_elementos}')