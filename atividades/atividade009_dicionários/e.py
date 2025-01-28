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

os.system('cls')

def listagem():
    os.system('cls')
    if cadastrados:
        print(f'Lista de alunos cadastrados: ')
        for matricula, dados in cadastrados.items():
            print(f'Matrícula: {matricula}, Nome: {dados["Nome"]},'
                    f' Data de Nascimento: {dados["Data de nascimento"]}')
    else:
        os.system('cls')
        print(f'Não existe nenhum aluno cadastrado')

def cadastrar():
    aluno = input(f'Nome: ').capitalize()
    data = input(f'data de nascimento(dd/mm/aaaa): ')
    numero_matricula = int(input(f'Número de matrícula: '))
    cadastrados[numero_matricula] = {'Nome': aluno, 'Data de nascimento': data}
    print('Aluno cadastrado.')
    input('Enter para continuar')
    os.system('cls')

def relatorio():
    os.system('cls')
    ano_2000 = 0
    matricula_impar = 0
    for matricula, info in cadastrados.items():
        nascimento = int(info['Data de nascimento'].split('/')[-1])
        if nascimento > 2000:
            ano_2000 += 1
        if matricula % 2 != 0:
            matricula_impar += 1
        print(f"Alunos nascidos após o ano 2000: {ano_2000}")
        print(f"Alunos com números de matrícula ímpares: {matricula_impar}\n")
    
def procurar_aluno():
    os.system('cls')
    if cadastrados:
        num_matricula = int(input('Insira o numero de '
                                    'matrícula do aluno: '))
        if num_matricula in cadastrados:
            dados = cadastrados[num_matricula]
            print(f'Número de Matrícula: {num_matricula}, '
                    f'Nome: {dados["Nome"]}, '
                    f'Data de Nascimento: {dados["Data de nascimento"]}')
    else:
        os.system('cls')
        print(f'Não existe nenhum aluno cadastrado.')

def mudar_dados():
    os.system('cls')
    for i, j in cadastrados.items():
        print(f'Aluno: {j["Nome"]}, Matrícula: {i}')
    if cadastrados:
        matricular = int(input('Número de matrícula do aluno: '))
        if matricular in cadastrados:
            os.system('cls')
            print(f'Dados atual: {cadastrados[matricular]}')
            mudar = input('Digite oque deseja modificar: ').lower()
            if mudar == 'data de nascimento':
                nova_data = input('Insira a Data de Nascimento(dd/mm/'
                                    'aaaa): ')
                cadastrados[matricular]['Data de nascimento'] = nova_data
            elif mudar == 'nome':
                novo_nome = input('Insira o nome: ').capitalize()
                cadastrados[matricular]['Nome'] = novo_nome
                print('Mudança feita.')
            else:
                print('Opção não encontrada.')
        else:
            print('Aluno não encontrado.')
    else:
        print('Ninguém cadastrado atualmente.')
    
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
        cadastrar()

    elif opcao == '2':
        mudar_dados()

    elif opcao == '3':
        listagem()
    
    elif opcao == '4':
        relatorio()

    elif opcao == '5':
        procurar_aluno()

    elif opcao == '6':
        print('Saindo...')
        break