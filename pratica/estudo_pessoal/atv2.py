import os


os.system('cls')

dia1 = int(input("número de livros emprestados na segunda: "))
dia2 = int(input("número de livros emprestados na terça: "))
dia3 = int(input("número de livros emprestados no quarta: "))
dia4 = int(input("número de livros emprestados no quinta: "))
dia5 = int(input("número de livros emprestados no sexta: "))

total = dia1 + dia2 + dia3 + dia4 +dia5
media = total / 5

if dia1 > dia2 and dia1 > dia3 and dia1 > dia4 and dia1 > dia5:
    print(f'O dia com o mais empréstimos é segunda: {dia1} ')
elif dia2 > dia3 and dia2 > dia4 and dia2 > dia5:
    print(f'O dia com mais empréstimos é terça: {dia2}')
elif dia3 > dia4 and dia3 > dia5:
    print(f'O dia com mais empréstimos é quarta: {dia3}')
elif dia4 > dia5:
    print(f'O dia com mais empréstimos é quinta: {dia4}')
elif dia1 == dia2 == dia3 == dia4 == dia5:
    print(f'Todos os dias são iguais')
else:
    print(f'O dia com mais empréstimos é sexta: {dia5}')

print(f'O total de livros emprestados é {total}')
print(f'A média é: {media}')