def Cadastrar_alunos(num_de_vezes):
    alunos = {}
    nome = input('Digite o nome do aluno: ')
    matricula = input(f'Matrícula: ')
    data_nascimento = input('Data de nascimento(dd/mm/aaaa): ')
    
    # Armazenando os dados do aluno
    alunos[matricula] = {'nome': nome, 'data_nascimento': data_nascimento}
    
    # Loop
    print("Alunos cadastrados:")
    for aluno, dados in alunos.items():
        print(f'Matrícula: {aluno}')
        print(f'Nome: {dados["nome"]}')
        print(f'Data de nascimento: {dados["data_nascimento"]}')
    
    return alunos