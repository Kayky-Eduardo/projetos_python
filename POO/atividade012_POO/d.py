# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.
import os

class Divisao:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b
    
    def set_a(self, value):
        self._a = value

    def set_b(self, value):
        self._b = value

    def dividir(self):
        if self._b != 0:
            divisao = self._a / self._b
            print(f'O valor da divisão é: {divisao:.4f}')
        else:
            print(f'Número inválido')
        return divisao
    

valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor: '))
objeto = Divisao(valor1, valor2)

os.system('cls')
objeto.dividir()