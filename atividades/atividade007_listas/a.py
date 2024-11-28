#Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.
import os


os.system('cls')

lista = []

print('Pressione "s" ou "0" para sair.')

#Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.
import os


os.system('cls')

lista = []
print('Digite "s" ou "0" para sair.')
while True:
    entrada = input('Digite a nota: ').lower().replace(' ', '')
    if entrada == 's' or entrada == '0':
        break
    elif not entrada.isnumeric():
        print('Inválido')
    else:
        num = int(entrada)
        lista.append(num)
if lista == []:
    print('Lista vazia.')
    exit()        
print(f'Quantidade de notas lidas: {len(lista)}')
print(f'A lista na ordem informada: {lista}')

print(f'Lista na ordem inversa: ')
for i in lista[::-1]:
    print(f'{i}')

soma = 0
for i in lista:
    soma += i
print(f'A soma das notas: {soma}')

media = soma / len(lista)
print(f'A media das notas: {media}')