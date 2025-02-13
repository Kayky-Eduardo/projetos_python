#Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra.
#Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.
import os


os.system('cls')

print('Estou em looping')

while (True):
    print('digite [f] para sair do loop.')
    nome = str(input('Digite uma letra: ')).lower()
    
    if (nome != 'f'):
        print('Continue digitiando...')
    else:
        print('='*70)
        print('Você digitou "f" para sair!')
        break
print('='*70)
print()

#for _ in range(100):
#    print('digite [f] para sair do loop.')
#    nome = str(input('Digite uma letra: ')).lower()
#    if nome != 'f':
 #       print('Continue digitiando...')
 #   else:
 #       print('='*70)
 #       print('Você digitou "f" para sair!')
 #       break
#print('='*70)
#print()