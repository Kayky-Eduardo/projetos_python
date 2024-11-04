import os
import math


os.system('cls')

valor = float(input('Insira um valor: '))

if valor < 0:
    print("O resultado será um número complexo.")
else:
    raiz_exata = math.sqrt(valor)
    raiz_baixo = math.floor(raiz_exata)
    raiz_superior = math.ceil(raiz_exata)
if raiz_exata == raiz_baixo == raiz_superior:
    print(f'A raiz quadrada exata de {valor} é: {raiz_baixo}')
else:
    print(f'A raiz quadrada de {valor} é {raiz_baixo} ou {raiz_superior}')