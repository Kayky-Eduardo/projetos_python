import os


os.system('cls')

nome = input('Nome completo: ')

separado = nome.split()
print(f'{separado}\n{separado[0]}\n{separado[1]}'
   f'{separado[2]}\n{separado[3]}')
#ou print(separado)