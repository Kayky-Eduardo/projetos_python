import os


os.system('cls')


from funcoes_usadas import calculo_media_peso_e_altura

while True:
    print('-'*70)
    comeco = input('Digite 1 para cadastrar e 0 para sair: ')

    if comeco == '1':
        nome = input('Digite seu nome: ')
        altura = float(input('Digite sua altura: '))
        peso = float(input('Digite seu peso: '))
        os.system('cls')
        num_alunos, media_altura, media_peso = calculo_media_peso_e_altura.media(nome, altura, peso)
        print('-'*70)
        print(f'Número de alunos: {num_alunos}')
        print(f'Média de altura: {media_altura:.2f}')
        print(f'Média de peso: {media_altura:.2f}')

    elif comeco == '0':
        break
    
    else:
        print(f'Opção inválida.')
        os.system('cls')