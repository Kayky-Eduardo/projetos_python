#import da biblioteca
import os

#limpeza do terminal
os.system('cls')

#entrada
print()
print('='*70)
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))
nota4 = float(input('digite a quarta nota: '))
print('='*70)

#processamento
media = (nota1 + nota2 + nota3 + nota4) / 4

#saida
print()
print('>'*70)
print(f'A média das suas notas é: {media}')
print('<'*70)
print()