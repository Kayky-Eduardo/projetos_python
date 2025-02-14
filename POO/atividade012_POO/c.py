#Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.
import os


class Media:
    def __init__(self):
        self._notas = []
    
    def get_notas(self):
        return self._notas
    
    def set_nota1(self, valor1):
        self._notas[0] = valor1
    
    def set_nota2(self, valor2):
        self._notas[1] = valor2

    def set_nota3(self, valor3):
        self._notas[2] = valor3

    def set_nota1(self, valor4):
        self._notas[3] = valor4

    def calcular_media(self):
        media = sum(self._notas) / len(self._notas)
        return media
    
    def adicionar_notas(self, nota):
        if nota > 0:
            self._notas.append(nota)
        else:
            print('Nota com valor a baixo do zero!')

notas = Media()
for i in range(4):
    nota = float(input(f'Digite a nota: '))
    notas.adicionar_notas(nota)

os.system('cls')
media = notas.calcular_media()
print(f'A média das notas é {media}')