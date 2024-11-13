import os


os.system('cls')

print('-'*50)
print('ESTRUTURA DE CONTROLE: CONTINUE')
print('='*50)

print()

for c in range(1, 11):
    if c == 5:
        # 5 está fora do loop, se retirar a linha abaixo,
        #ele não aparecerá na saída, deixei para verificação!
        print(f'O número {c} está fora do loop')
        continue # Salta e o ciclo continua
    
    print(f'O número é {c}')

print('-'*70)
print()