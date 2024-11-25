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

while(True):
    numeros = (input('Digite os numeros: ')).lower()
    if numeros == 's':
        break
    else:
        troca = int(numeros)
    if troca == 0:
        break
    else:
        lista.append(troca)

print('Lista inversa:')
for i in lista[::-1]:
    print(f'{i}')
    
soma = 0
for i in lista:
    soma += i

media = soma / len(lista)

print(f'Foram lidas {len(lista)} notas.')
print(F'lista: {lista}')
print(f'A soma das notas é: {soma}')
print(f'A media das notas é: {media}')