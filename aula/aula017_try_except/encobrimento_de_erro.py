try:
    # Código que pode gerar várias exceções
    Resultado = 10 / 0
    arquivo = open('arquivo_inexistente.txt', 'r')
except Exception:
    # Captura todas as exceções, mas não faz nada com elas
    pass

print('Continua a execução do programa.')