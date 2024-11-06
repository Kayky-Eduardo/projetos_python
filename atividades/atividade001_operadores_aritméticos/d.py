#biblioteca
import os

#limpeza do terminal
os.system('cls')

#Entrada
divisor = float(input('Entre com o 1ª valor: '))
dividendo = float(input('Entre com o 2ª valor: '))
print('-'*70)

#processamento
resultado = divisor / dividendo


#saída
print(f'O resultado dessa divisão é {resultado:.4f}')