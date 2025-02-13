import os
from funcoes_usadas import cadastrar

os.system('cls')


num_de_vezes = int(input("Quantos alunos deseja cadastrar? "))
cadastrar.Cadastrar_alunos(num_de_vezes)