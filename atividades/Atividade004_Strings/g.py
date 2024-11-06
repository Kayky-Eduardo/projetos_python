import os


os.system('cls')

num = (input('Insira algum número inteiro: '))

separar = ' '.join(num)

print(f'Unidades:{separar[0]}')
print(f'Dezenas:{separar[2]}')
print(f'Centenas:{separar[4]}')
print(f'Milhares: {separar[6]}')