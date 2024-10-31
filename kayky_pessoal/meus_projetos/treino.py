import os


os.system('cls')

a = int(input('Digite o valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
auxiliar = 0

if a > b or a > c:
    if b < c:
        auxiliar = a
        a = b
        b = auxiliar
    else:
        auxiliar = a
        a = c
        c = auxiliar
if b > c:
    auxiliar = b
    b = c
    c = auxiliar
print(f'{a}, {b} e {c}')
    