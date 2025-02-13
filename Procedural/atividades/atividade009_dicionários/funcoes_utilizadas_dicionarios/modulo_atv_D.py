def listagem(dicio):
    if dicio:
        for nome, info in dicio.items():
            # breve explicação para caso eu me esqueça
            # nome vai virar o dicionario q está dentro do dicionario e eu vou buscar os dados dele por info
            # poderia fazer de um jeito mais curto igual no 2 mas assim fica mais bonito
            print('-'*70)
            print(f'{nome}:\nTipo: {info["Tipo"]}\n'
                f'Teor alcoólico: {info["Teor alcoólico"]}%\n'
                f'Safra: {info["Safra"]}')
    else:
        print('Lista vazia.')    
        
def mudar_dados(dicio):
    if dicio:
        listagem(dicio)
        nome_vinho = input('\nQual vinho deseja modificar: ').capitalize()
        if nome_vinho in dicio:
            mudar = input('Digite oque deseja modificar: ').capitalize()
            if mudar in dicio[nome_vinho]:
                novo = input('Digite o que deseja colocar no lugar: ')
                dicio[nome_vinho][mudar] = novo
                print('Mudança feita.')
            else:
                print('Classificação não encontrada.')
        else:
            print('Vinho não encontrado.')
    else:
        print('Nada cadastrado atualmente.')

def relatorio(dicio):
    if dicio:
        cont_teor = 0
        cont_safra = 0
        for dados in dicio.values():
            if dados['Teor alcoólico'] > 12:
                cont_teor += 1
            if dados['Safra'] > 2015:
                cont_safra += 1
        print(f'Temos {cont_teor} vinhos com mais de 12% de '
                'teor Alcoólico.')
        print(f'Temos {cont_safra} vinhos com Safra superior a de 2015. ')
        