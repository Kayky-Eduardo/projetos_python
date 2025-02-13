#Desenvolva um programa para cadastrar alunos de uma escola, onde cada aluno
#terá os seguintes dados: nome, data de nascimento e número de matrícula. O
#programa deve permitir que o usuário cadastre ao menos 5 alunos, com essas
#informações, e possibilitar a alteração de dados já cadastrados, caso 
#necessário. Após o cadastro, o programa deve exibir uma lista com todos os 
#alunos registrados, mostrando o nome, a data de nascimento e a matrícula de
#cada um. Além disso, o programa deve gerar um relatório que informe quantos 
#alunos nasceram após o ano de 2000 e quantos possuem números de matrícula
#ímpares. Por fim, o programa deve permitir que o usuário busque e exiba
#informações de um aluno específico a partir de seu número de matrícula, 
#garantindo que os dados inseridos estejam corretos
import os
from funcoes_utilizadas_dicionarios import modulo_atv_E


os.system('cls')


cadastrados = {}

while True:
    print('-'*70)
    print('1. Cadastrar aluno.')
    print('2. Alteração de dados.')
    print('3. Lista com alunos cadastrados.')
    print('4. Relatório de informações dos alunos.')
    print('5. Procurar aluno por número de matrícula')
    print('6. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        os.system('cls')
        modulo_atv_E.cadastrar(cadastrados)
        
    elif opcao == '2':
        os.system('cls')
        modulo_atv_E.mudar_dados(cadastrados)

    elif opcao == '3':
        os.system('cls')
        modulo_atv_E.listagem(cadastrados)
    
    elif opcao == '4':
        os.system('cls')
        modulo_atv_E.relatorio(cadastrados)

    elif opcao == '5':
        os.system('cls')
        modulo_atv_E.procurar_aluno(cadastrados)

    elif opcao == '6':
        print('Saindo...')
        break