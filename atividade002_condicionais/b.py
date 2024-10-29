
import os


os.system('cls')

#entrada
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

#condicional igual
if num1 == num2 == num3:
    print('Todos os números são iguais')
else:
#condicional maior que
    if num1 > num2 and num1 > num3:
        print(f'{num1} é o maior numero')
    elif num2 > num3:
        print(f'{num2} é o maior numero')
    else:
        print(f'{num3} é o maior numero')
    
#condicional menor que
    if num1 < num2 and num1 < num3:
        print(f'{num1} é o menor numero')
    elif num2 < num3:
        print(f'{num2} é o menor numero')
    else:
        print(f'{num3} é o menor numero')
