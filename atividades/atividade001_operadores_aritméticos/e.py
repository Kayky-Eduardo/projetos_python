#importando biblioteca
import os

#limpeza do terminal
os.system('cls')

#entrada
valor = int(input('Digite o número: '))

#processamento
antecessor = (valor - 1)
sucessor = (valor + 1)

#saída
print(f'O antecessor é {antecessor}, e o sucessor é {sucessor}')