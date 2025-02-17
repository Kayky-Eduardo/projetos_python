import os
import math


class Equacao:
    def __init__(self, a=1, b=0, c=0):
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
    def set_a(self, value):
        self._a = value

    def set_b(self, value):
        self._b = value

    def set_c(self, value):
        self._c = value

    def calcular_raizes(self):

        # Calculando o delta
        delta = self._b ** 2 -4 * self._a * self._c

        if delta < 0:
            return 'A equação não possui raizes reais.'
        elif delta == 0:
            raiz = -self._b / (2 * self._a)
            return f'A equação possui uma raiz real: {raiz}'
        else:
            x1 = (-self._b + math.sqrt(delta)) / (2 * self._a)
            x2 = (-self._b - math.sqrt(delta)) / (2 * self._a)
            return f'A equação possui duas raízes reais: {x1} e {x2}'
        
os.system('cls')

print('-'*70)
print('Cálculo de equação do 2° Grau')
print('='*70)
equacao1 = Equacao(1, -3, 2)
print(equacao1.calcular_raizes())

print('-'*70)
print('Cálculo de equação do 2°Grau')
equacao1.set_a(1)
equacao1.set_b(2)
equacao1.set_c(1)
print(equacao1.calcular_raizes())
print('-'*70)