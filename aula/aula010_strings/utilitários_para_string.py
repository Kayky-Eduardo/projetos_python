import os


os.system('cls')

print('-'*70)
print('Operadores úteis para')
print('Strings e Estruturas de Dados')
print('='*70)

texto = 'Olá, Mundo!'

print(f'Texto: {texto}')
if 'Mundo' in texto: # Verifica a palavra dentro da string
    print('A palavra "Mundo" está presente na string.')
else:
    print('A palavra "Mundo" não está presente na string.')
    
print('.'*70)

texto2 = 'Olá, Python!'

print(f'Texto: {texto2}')
if 'Mundo' not in texto2: # Verifica a palavra dentro da string
    print('A palavra "Mundo" não está presente na string.')
else:
    print('A palavra "Mundo" está presente na string.')

print('.'*70)