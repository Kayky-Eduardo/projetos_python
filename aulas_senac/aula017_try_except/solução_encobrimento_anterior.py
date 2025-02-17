try:
    # Código que pode gerar várias exceções
    resultado = 10 / 0
    arquivo = open('arquivo_inexistente.txt', 'r')
except ZeroDivisionError:
    print('Erro: Divisão por zero!')
except FileNotFoundError:
    print('Erro: Arquivo não encontrado!')
except Exception as e:
    # Captura outras exceções e imprime a mensagem de erro
    print(f'Erro inesperado: {e}')

print('Continua a execução do programa')