import os
import math


os.system('cls')

valor = float(input('Insira um valor: '))

if valor < 0:
    print("O resultado será um número complexo.")
else:
    raiz = math.sqrt(valor)
    baixo = math.floor(raiz)
    cima = math.ceil(raiz)
    if raiz == baixo == cima:
        print(f'A raiz quadrada exata de {valor} é: {raiz}')
    else:
        print(f'A raiz quadrada de {valor} é {baixo} ou {cima}')