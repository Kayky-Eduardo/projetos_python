def exibir_resultados(estudantes):
    for estudante in estudantes:
        print(f'\nNome: {estudante.nome}')
        print(f'Idade: {estudante.idade}')
        print(f'Média: {estudante.media():.2f}')
        print(f'Resultado: {estudante.resultado()}')
        