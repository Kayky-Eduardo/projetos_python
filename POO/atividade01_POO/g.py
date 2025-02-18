# Faça um programa que converta metros em centímetros e milímetros.
import os


os.system('cls')

class Convercao:
    def __init__(self, metros):
        self._metros = metros

    def get_metros(self):
        return self._metros
    
    def set_metros(self, valor):
        self._metros = valor

    def metros_centímetros(self):
        cm = self._metros * 100
        return cm
    
    def metros_milimitros(self):
        mm = self._metros * 1000
        return mm
    
metros = float(input('Digite um número: '))

objeto = Convercao(metros)

centimetros = objeto.metros_centímetros()
milimetros = objeto.metros_milimitros()

print(f'Valor em metros: {metros}\nValor em centímetros: {centimetros}cm\n'
      f'Valor em milímetros: {milimetros}')