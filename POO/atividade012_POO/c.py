#Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.
class Media:
    def __init__(self, nota1, nota2, nota3, nota4):
        self._notas = []
    
    def Calcular_media(self):
        media = sum(self._lista) / len(self._lista)
        return media
    
    def set_nota(self, nota):
        if nota > 0:
            self._notas.append(nota)
        else:
            print('Nota com valor a baixo do zero!')

notas = Media()
for i in range(4):
    nota = float(input(f'Digite a nota: '))
    notas.set_nota(nota)