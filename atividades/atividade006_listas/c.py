#Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
#• O intervalo de 1 até 9
#• O intervalo de 8 até 13
#• Os números pares
#• Os números ímpares
#• Os múltiplos de 2, 3 e 4
#• Lista reversa
#• O produto dos intervalos 5-6 por 11-12
import os


os.system('cls')

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(f'Intervalo de 1 até 9: {lista_numeros[0:9]}')
print(f'Intervalo de 1 até 9: {lista_numeros[8:13]}')
print(f'Números pares: {lista_numeros[2:15:2]}')
print(f'Números ípares: {lista_numeros[1:15:2]}')

print('Os números mutiplos de 2,3 e 4 são:')
for i in lista_numeros:
    if i % 2 == 0 or i % 3 == 0 or i % 4 == 0:
        print(i, end=' ')

lista_reversa = lista_numeros.reverse()
print(f'Lista reversa: {lista_reversa}')
