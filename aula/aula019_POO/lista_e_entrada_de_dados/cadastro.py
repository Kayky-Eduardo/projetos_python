from estudante import Estudante

def cadastrar_estudante():
    nome = input('Digite o nome do estudante: ')
    idade = int(input(f'Digite a idade de {nome}: '))
    
    estudante = Estudante(nome, idade)
    while True:
        try:
            nota = float(input(f'Digite a nota de {nome} (ou 0) para terminar: '))
            if nota == 0:
                break
            estudante.adicionar_nota(nota)
        except ValueError:
            print('Por favor, digite uma nota válida.')  
    return estudante