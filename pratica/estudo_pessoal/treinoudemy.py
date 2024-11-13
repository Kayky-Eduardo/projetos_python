import os

os.system('cls')

nome = 'Luiz Otavio'
a = 0
texto = len(nome)
resultado = "*"

while a < texto:
    resultado += nome[a] + '*'
    a += 1
print(resultado)
