# Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.
import os


os.system('cls')

class Tabuada:
    def __init__(self, numero):
        self._num = numero

    def get_num(self):
        return self._num
    
    def set_num(self, valor):
        self._num = valor

    def fazer_tabuada(self):
        for i in range(1, 11):
            mult = 0
            mult = self._num * i
            print(f'{self._num} * {i} = {mult}')
        return
    
entrada = int(input('Digite um número para tabuada: '))
objeto = Tabuada(entrada)

objeto.fazer_tabuada()