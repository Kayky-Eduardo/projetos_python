# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.
import os


os.system('cls')

class Numero:
    def __init__(self, numero):
        self._numero = numero

    def get_numero(self):
        return self._numero
    
    def set_numero(self, valor):
        self._numero = valor

    def suscessor_antecessor(self):
        antecessor = self._numero - 1
        sucessor = self._numero + 1
        return antecessor, sucessor
    
entrada = int(input('Digite um número: '))
objeto = Numero(entrada)
antecessor, sucessor = objeto.suscessor_antecessor()


print(f'Numero: {entrada}\nSucessor: {sucessor}\nAntecessor: {antecessor}')