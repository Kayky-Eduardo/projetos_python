import os 


os.system('cls')

ano = int(input('Insira o ano: '))

if ano <= 0:
    print('Este não é um ano válido.')
else:
    if (ano % 4 == 0 and ano %100 != 0) or (ano % 400 == 0):
        print(f'O ano {ano} é um ano bissexto!')
    else:
        print(f'O ano {ano} não é um ano bissexto!')