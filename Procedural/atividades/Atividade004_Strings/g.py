import os


os.system('cls')

num = (input('Insira algum número inteiro: '))

separar = ' '.join(num)

print(f'Unidades:{separar[6]}')
print(f'Dezenas:{separar[4]}')
print(f'Centenas:{separar[2]}')
print(f'Milhares: {separar[0]}')