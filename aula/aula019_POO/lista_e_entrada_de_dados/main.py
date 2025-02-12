import os
from cadastro import cadastrar_estudante
from resultado import exibir_resultados

def main():
    os.system('cls')
    print('Cadastro Alunos')
    print('-'*70)
    
    # Lista para armazenar os estudantes cadastrado
    estudantes = []
    
    while True:
        # Chama a função para cadastrar um novo estudante
        estudante = cadastrar_estudante()
        estudantes.append(estudante)
        
        continuar = input('Deseja cadastrar outro estudante? (s/n): ').lower()
        if continuar != 's':
            break
        
    # Exibe os resultados de todos os estudantes cadastrados
    exibir_resultados(estudantes)
    
# Bloco que garante que a função main() só será executada
# quando o arquivo for executado diretamente e não quando for importado como módulo
if __name__ == '__main__':
    main()