import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE WHILE ELSE BREAK')
print('='*70)

print()

while (True):
    
    nome = str(input('Digite um nome [s - Sair]: ')).lower()
    
    if (nome != 's'):
        print('Continue digitiando...')
    else:
        print('-'*70)
        print('Você digitou "s" para sair!')
        
        break

print('-'*70)
print()