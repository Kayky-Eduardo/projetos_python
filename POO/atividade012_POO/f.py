# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.
import os


os.system('cls')

class Calcular:
    def __init__(self, num):
        self._num = num

    def get_num(self):
        return self._num
    
    def set_num(self, valor):
        self._num = valor
    
    def calcular_dobro(self):
        dobro = self._num * 2
        return dobro

    def calcular_triplo(self):
        triplo = self._num * 3
        return triplo
    
entrada = float(input('Digite um número: '))
objeto = Calcular(entrada)

dobro = objeto.calcular_dobro()
triplo = objeto.calcular_triplo()

print(f'Dobro de {entrada}: {dobro:.2f}\nTriplo de {entrada}: {triplo:.2f}')