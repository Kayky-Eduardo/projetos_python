#Faça um programa que imprima os números pares entre 0 e 100.

for i in range(0, 100 + 1):
    if i % 2 == 0:
        print(f'{i}', end= ' | ')
        if i % 10 == 0:
            print('\n')
print('Acabou!')