# e) 
# Desenvolva um programa para cadastrar alunos de uma escola, onde cada aluno
# terá os seguintes dados: nome, data de nascimento e número de matrícula. O
# programa deve permitir que o usuário cadastre ao menos 5 alunos, com essas
# informações, e possibilitar a alteração de dados já cadastrados, caso 
# necessário. Após o cadastro, o programa deve exibir uma lista com todos os 
# alunos registrados, mostrando o nome, a data de nascimento e a matrícula de
# cada um. Além disso, o programa deve gerar um relatório que informe quantos 
# alunos nasceram após o ano de 2000 e quantos possuem números de matrícula
# ímpares. Por fim, o programa deve permitir que o usuário busque e exiba
# informações de um aluno específico a partir de seu número de matrícula, 
# garantindo que os dados inseridos estejam corretos
import os


os.system('cls')

dicio = {}

while True:
    print('-'*70)
    print('1. Cadastrar aluno.')
    print('2. Alteração de dados.')
    print('3. Lista com alunos registrados.')
    print('4. Relatório de informações dos alunos.')
    print('5. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
            aluno = input(f'Nome: ').capitalize()
            data = int(input(f'data de nascimento: '))
            num_matricula = float(input(f'Número de matrícula: '))
            dicio[aluno] = {'Data de Nascimento': data,'Número de matrícula': num_matricula}
            print('Aluno cadastrado.')
            input('Enter para continuar')
            os.system('cls')

    elif opcao == '2':
        if dicio:
            nome_vinho = input('Qual vinho deseja modificar: ').capitalize()
            if nome_vinho in dicio:
                mudar = input('Digite oque deseja modificar: ').lower()
                if mudar == 'data de nascimento':
                    nova_data = input('Insira o novo tipo: ')
                    dicio[nome_vinho]['Data de Nascimento'] = nova_data
                elif mudar == 'número de matrícula':
                    novo_num = input('Insira o novo Teor alcoólico: ')
                    dicio[nome_vinho]['Número de matrícula'] = novo_num
                print('Mudança feita.')
            else:
                print('Aluno não encontrado.')
        else:
            print('Nada cadastrado atualmente.')