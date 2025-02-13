# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.
import os
from datetime import datetime


os.system('cls')

class Idade:
    def __init__(self, data_nascimento):
        # Chama o setter para definir a data de nascimento
        self.set_nascimento(data_nascimento)

    def set_nascimento(self, data_de_nascimento):
        self._data_nascimento = data_de_nascimento
        
        # Pega a data atual
        hoje = datetime.now()

        # Objeto de datetime
        nascimento = datetime.strptime(data_de_nascimento, '%d/%m/%Y')

        self._idade = hoje.year - nascimento.year \
        ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    def get_idade(self):
        return self._idade
    
data_de_nascimento = input('Digite sua data de nascimento(dd/mm/yyyy): ')
pessoa1 = Idade(data_de_nascimento)
idade = pessoa1.get_idade()

print(f'Voce possui {pessoa1} anos')