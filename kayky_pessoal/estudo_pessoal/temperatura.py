
import os
os.system('cls')

# Recebendo uma palavra ou frase do usuário
entrada = input("Digite uma palavra ou frase: ")

# Removendo espaços e convertendo para minúsculas
entrada = entrada.replace(" ", "").lower()

# Comparando a string com sua reversa
if entrada == entrada[::-1]:
    print("A entrada é um palíndromo.")
else:
    print("A entrada não é um palíndromo.")