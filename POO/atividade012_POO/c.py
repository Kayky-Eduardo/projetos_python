#Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.
class Media:
    def __init__(self, nota1, nota2, nota3, nota4):
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3
        self._nota4 = nota4
        self._lista = []
    
    def Calcular_media(self):
        media = sum(self._lista) / len(self._lista)
        return media
    
    def adicionar_nota(self, nota):
        self._lista.append(nota)

nota1 = int(input('Digite o primeiro valor: '))
nota2 = int(input('Digite o segundo valor: '))
nota3 = int(input('Digite o terceiro valor: '))
nota4 = int(input('Digite o qurto valor: '))

notas = Media()
for i in range(4):
    nota = float(input(f'Digite a nota: '))

    lista.adicionar_nota(nota)