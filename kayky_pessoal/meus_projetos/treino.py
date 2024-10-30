import os


os.system('cls')

a = int(input('Digite o valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))


if a > b or a > c:
    if b > c:
        auxiliar = a
        a = b
        b = auxiliar
    else:
        b < c
        auxiliar = a
        a = c
        c = auxiliar
    print(f'{a},{b} e {c}')
else:
    print()