import os


os.system('cls')

for i in range(1, 100):
    num = input('Digite um número inteiro: ')
    if num == 's':
        print('Você está saindo')
        break
    convercao = float(num)
    if num.isdigit():
        print('Você digitou um inteiro')
        par = convercao % 2 == 0
        if par:
            print('O número é par!')
        else:
            print('O número é impar!')
    else:
        print('Este numero não é inteiro')