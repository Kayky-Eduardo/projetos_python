import os
os.system('cls')

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('seu nome possui espaços')
    else:
        print('seu nome não possui espaços')
        
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é: {nome[0]}')
    print(f'a ultima letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')