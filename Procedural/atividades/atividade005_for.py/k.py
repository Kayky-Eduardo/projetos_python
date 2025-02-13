import os #Crie um programa que pede que o usuário digite um frase ou uma frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.


os.system('cls')

frase_invertida = ''
frase = input('Digite uma frase: ').lower().replace(' ', '')
for letra in frase[::-1]:
    frase_invertida += letra
    if frase == frase_invertida:
        print(f'A frase é um palíndromo')
    else:
        print(f'A frase não é um palíndromo')   