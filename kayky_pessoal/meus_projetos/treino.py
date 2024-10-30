import os


os.system('cls')

salario = float(input('Insira seu salário: '))

if salario <= 0:
    print('Erro!')
elif salario >= 3000:
    imposto = salario * 0.20
    print(f'o imposto cobrado foi de {imposto:.2f}')
else:
    print('Isento de imposto')