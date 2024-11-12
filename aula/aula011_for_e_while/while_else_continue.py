import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE WHILE ELSE CONTINUE')
print('='*70)

print()

contador = 0 # Flag

while (contador <= 10):
    
    # Soma o contador
    contador += 1 
    
    if (contador % 2 == 0):
        continue
    print(f'Contador = {contador}')
else:
    print(f'Bloco do while...else: contador em {contador}!')

print('-'*70)
print('Fim do programa!')
print()