import os
import math


#limpando o terminal
os.system('cls')

print('ESTUDO DA BIBLIOTECA MATH')
print()

#Declarações
base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5 #cat oposto
ca = 10 #cat adjacente

#processamento
potencia = math.pow(base, expoente)
raizquadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co, ca)

#saída
print(f'{base} elevado a {expoente} é igual a: {potencia}')
print(f'A raiz quadrada de {radicando} é: {raizquadrada}')
print(f'O seno de {angulo} é: {seno:.2f}')
print(f'O cosseno de {angulo} é: {cosseno:.2f}')
print(f'A tangente de {angulo} é: {tangente:.2f}')
print(f'o valor da hipotenusa é: {hipotenusa:.2f} ')
print('-'*70)