# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.
import os


os.system('cls')

class Retangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
    
    def get_base(self):
        return self._base
    
    def get_altura(self):
        return self._altura
    
    def set_base(self, valor):
        self._base = valor
    
    def set_base(self, valor):
        self._base = valor

    def calcular_perimetro(self):
        perimetro = 2 * (self._base + self._altura)
        return perimetro
    
base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))

retangulo = Retangulo(base, altura)

perimetro = retangulo.calcular_perimetro()

print(f'base: {retangulo.get_base()}')
print(f'Altura: {retangulo.get_altura()}')
print(f'Perímetro: {perimetro}')