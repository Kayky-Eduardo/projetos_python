import os


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        return 'Isto está no método latir()'
    
    def miar():
        return 'Isto está no método miar()'
    

class Cachorro(Animal):
    def latir(self):
        return f'{self.nome} está latindo'
    
class Gato(Animal):
    def miar(self):
        return f'{self.nome} esta miando'
    

os.system('cls')
cao = Cachorro('Rex')
gato = Gato('Tobias')
print(cao.latir())
print(gato.miar())