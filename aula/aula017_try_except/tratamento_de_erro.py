import os


os.system('cls')

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print('Erro: Divisão por Erro!')
else:
    print('Tudo ok! Divisão realizada com sucesso!')
finally:
    print('Este bloco é sempre executado.')