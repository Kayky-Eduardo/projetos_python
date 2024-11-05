import os


os.system('cls')

nome = input('Digite o seu nome: ')

menor = nome.lower()

if 'oliveira' in menor:
    print('A palavra oliveira está dentro do nome!')
else:
    print('A palavra oliveira não está dentro do nome!')