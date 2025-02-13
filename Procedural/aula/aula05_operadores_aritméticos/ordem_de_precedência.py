import os

os.system('cls')

print('-'*70)
print('Operadores Aritmético: Ordem de Precedência')
print('-'*70)

#entrada
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

#processamento
soma = nota1 + nota2 + nota3 + nota4
media = nota1 + nota2 + nota3 + nota4 / 4
media_correta = soma / 4

#saida
print('---- Notas --------')
print(f'Nota 1: {nota1} | Nota 2: {nota2} | '
      f'Nota 3: {nota3} | Nota 4: {nota4}')
print('-'*70)
print(f'Média errada: {media}')
print(f'Média correta: {media_correta}')
print('-'*70)