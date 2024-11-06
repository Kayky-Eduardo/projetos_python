import os


os.system('cls')

aluno = input('Nome do aluno: ')
menor = aluno.lower()
o = menor.count('o')

if 'o' in menor:
    primeira = menor.find('o')
    ultima = menor.rfind('o')
    print(f'o número de vezes que a letra o apareceu foi de: {o}')
    print(f'Ele aparece pela primeiras vez em {primeira}')
    print(f'Ele aparece pela ultima vez em: {ultima}')
else:
    print(f'A letra "o" não apareceu no nome do aluno.')