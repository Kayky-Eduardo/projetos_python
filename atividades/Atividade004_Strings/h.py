import os


os.system('cls')

aluno = str(input('Nome do aluno: ')).lower()
o = aluno.count('o')

if 'o' in aluno:
    primeira = aluno.find('o') + 1
    ultima = aluno.rfind('o') + 1
    print(f'o número de vezes que a letra o apareceu foi de: {o}')
    if primeira == ultima:
        print(f'A letra o apareceu pela primeira e ultima vez no: {primeira}')
    else:
        print(f'Ele aparece pela primeiras vez em {primeira}')
        print(f'Ele aparece pela ultima vez em: {ultima}')
else:
    print(f'A letra "o" não apareceu no nome do aluno.')