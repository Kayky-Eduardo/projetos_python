# Solicitar ao usuário a quantidade de elementos da tupla
import os


os.system('cls')

# Solicitar ao usuário a quantidade de elementos na tupla
numeros_elementos = int(input('Quantos elementos na tupla? '))

# Inicializar uma lista vazia para armazenar os elementos
elementos = []

# Estrutura de repetição para obter os elementos do usuário
for i in range(numeros_elementos):
    while True:
        valor = input(f'Digite o valor {i + 1}: ')
        if valor.isdigit(): # Verifica se a entrada é um número
            elementos.append(int(valor))
            break
        else:
            print('Entrada inválida. Digite um número.')
# Converter a lista para uma tupla
tupla = tuple(elementos)

print('-'*70)
# Exibir a tupla criada
print(f'Tupla criada: {tupla}')
print('-'*70)

# Estrutura de repetição para permitir múltiplas
# operações até que o usuário deseje sair
while True:
    # Condicional para verificar a presença de
    # um número específico
    valor = int(input('Verificar se o número está na Tupla: '))
    
    if valor in tupla:
        print(f'O número {valor} está na tupla.')
        # Contar quantas vezes o número aparece
        contagem = tupla.count(valor)
        print(f'O número {valor} aparece {contagem} vez(es).')
        # Encontrar o Índice da primeira ocorrência
        
        indice = tupla.index(valor)
        print(f'A 1ª ocorrência de {valor} está no índice {indice}.')
    else:
        print(f'O número {valor} não está na tupla.')
        
    # Perguntar ao usuário se deseja realizar
    # outra operação ou sair
    
    continuar = input('Deseja Continuar? (s/n): ').lower()
    if continuar != 's':
        print('Encerrando o programa. Até mais!')
        break
print('-'*70)
print('Fim do programa!')
print()