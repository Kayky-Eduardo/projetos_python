# Você foi designado para desenvolver um sistema de cadastro de veículos para uma locadora de carros.
# A empresa possui diversos combustivels de veículos, como carros, motos e caminhões. 
# Todos os veículos possuem características em comum, como marca, modelo, ano e cor, mas cada combustivel de veículo tem atributos e comportamentos específicos.
# Para isso, você deve criar uma classe base chamada Veículo, que contenha esses atributos comuns e um método para exibir suas informações.
# Em seguida, você deve criar subclasses para Carro, Moto e Caminhão, que herdem da classe Veículo, adicionando atributos específicos de cada combustivel,
# como o combustivel de combustível para o carro, o combustivel de moto (esportiva, custom) e a capacidade de carga para o caminhão.
# O objetivo é garantir que o sistema consiga gerenciar diferentes combustivels de veículos de forma eficiente e sem duplicação de código,
# utilizando os conceitos de herança e polimorfismo.
import os
from modulo.menu import exibir_menu

os.system('cls')

if __name__ == '__main__':
    exibir_menu()