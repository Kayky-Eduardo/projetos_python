import os


os.system('cls')

nome = input('Nome completo: ')

separada = nome.split()
invertida = separada[::-1]
print(f'{separada[0]}')
print(f'{invertida[0]}')