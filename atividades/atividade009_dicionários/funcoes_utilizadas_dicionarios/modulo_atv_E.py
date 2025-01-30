def listagem(cadastrados):
    if cadastrados:
        print(f'Lista de alunos cadastrados: ')
        for matricula, dados in cadastrados.items():
            print(f'Matrícula: {matricula}, Nome: {dados["Nome"]},'
                    f' Data de Nascimento: {dados["Data de nascimento"]}')
    else:
        print(f'Não existe nenhum aluno cadastrado')

def cadastrar(cadastrados):
    aluno = input(f'Nome: ').capitalize()
    data = input(f'data de nascimento(dd/mm/aaaa): ')
    numero_matricula = int(input(f'Número de matrícula: '))
    cadastrados[numero_matricula] = {'Nome': aluno, 'Data de nascimento': data}
    print('Aluno cadastrado.')
    input('Enter para continuar')

def relatorio(cadastrados):
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
    
def procurar_aluno(cadastrados):
    if cadastrados:
        num_matricula = int(input('Insira o numero de '
                                    'matrícula do aluno: '))
        if num_matricula in cadastrados:
            dados = cadastrados[num_matricula]
            print(f'Número de Matrícula: {num_matricula}, '
                    f'Nome: {dados["Nome"]}, '
                    f'Data de Nascimento: {dados["Data de nascimento"]}')
    else:
        print(f'Não existe nenhum aluno cadastrado.')

def mudar_dados(cadastrados):
    for i, j in cadastrados.items():
        print(f'Aluno: {j["Nome"]}, Matrícula: {i}')
    if cadastrados:
        matricular = int(input('Número de matrícula do aluno: '))
        if matricular in cadastrados:
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
    