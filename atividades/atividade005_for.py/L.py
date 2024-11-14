#Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.
import os


os.system('cls')

usuario_c = "ojonasébrabo"
senha_c = "davidemeloferreira13@gmail.com"

for a in range(100):
    print('Digite "sair" para cancelar o login.')
    usuario = str(input('Digite o nome de usuário: ')).lower()
    senha = str(input('Digite a senha: ')).lower()
    if usuario == 'sair':
        print('Saindo...')
        break
    if usuario != usuario_c or senha != senha_c:
        print('Usuário ou senha incorreto')
    else:
        print('Conexão concluida.')
        break