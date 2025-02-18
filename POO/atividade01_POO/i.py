# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.
import os


os.system('cls')

class Convercao:
    def __init__(self, reais):
        self._reais = reais
        self._dolar = 5.73

    def comprar_dolar(self):
        return self._dolar / self._reais

    def set_reais(self, valor):
        self._reais = valor

    def get_reais(self):
        return self._reais
    
    def get_dolar(self):
        return self._dolar
    
reais = float(input('Digite um valor: '))
objeto = Convercao(reais)

valor_dolar = objeto.comprar_dolar()

print(f'Com {reais} reais você conseguiu comprar {valor_dolar} dólares')