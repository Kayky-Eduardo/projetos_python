import os


os.system('cls')

#entrada
salario = float(input('Insira o sálario atual: '))

#condicional
if salario >= 1500.00:
    bônus = salario * 0.05
else:
    salario <= 1000.00
    bônus = salario * 0.10

novo_salario = salario + bônus
if novo_salario <= 0:
    print('Não vai ter nenhum bônus.')
else:
    print(f'O sálario após o bonus séra {novo_salario:.2f}')