#Faça um programa que peça 3 valores, depois calcule e imprima  a soma e a multiplicação desses valores. 
import os


os.system('cls')

class Calcular:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # Getters
    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    # Setters
    def set_valores(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        
    def calcular_soma_mutiplicacao(self):
        soma = self._a + self._b + self._c
        mutiplicacao = (self._a * self._b * self._c)
        return soma, mutiplicacao


valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

calculo = Calcular(valor1, valor2, valor3)
soma, mutiplicacao = calculo.calcular_soma_mutiplicacao()

print(f'A soma dos números é: {soma}')
print(f'A mutiplicação dos números é: {mutiplicacao}')
print('='*70)

calculo.set_a(1)
calculo.set_b(2)
calculo.set_c(3)

print(f'A soma dos números é: {soma}')
print(f'A mutiplicação dos números é: {mutiplicacao}')
