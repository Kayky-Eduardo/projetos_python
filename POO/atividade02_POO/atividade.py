# Você foi designado para desenvolver um sistema de cadastro de veículos para uma locadora de carros.
# A empresa possui diversos tipos de veículos, como carros, motos e caminhões. 
# Todos os veículos possuem características em comum, como marca, modelo, ano e cor, mas cada tipo de veículo tem atributos e comportamentos específicos.
# Para isso, você deve criar uma classe base chamada Veículo, que contenha esses atributos comuns e um método para exibir suas informações.
# Em seguida, você deve criar subclasses para Carro, Moto e Caminhão, que herdem da classe Veículo, adicionando atributos específicos de cada tipo,
# como o tipo de combustível para o carro, o tipo de moto (esportiva, custom) e a capacidade de carga para o caminhão.
# O objetivo é garantir que o sistema consiga gerenciar diferentes tipos de veículos de forma eficiente e sem duplicação de código,
# utilizando os conceitos de herança e polimorfismo.
import os



class Veiculo:
# O dicionário veiculos é declarado antes do método construtor porque ele é um atributo de classe,
# e não um atributo de instância.
# Atributos de classe são compartilhados entre todas as instâncias de uma classe.
# Eles pertencem à classe em si e não a objetos individuais.
# Atributos de instância são específicos de cada objeto criado a partir da classe.
# Cada instância tem sua própria cópia desses atributos.

    veiculos = {'Carro': {}, 'Moto': {}, 'Caminhão': {}}
    
    def __init__(self, marca, modelo, cor, ano):
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._ano = ano

    def exibir_info(self):
        pass

    def receber_dados(self):
        pass

    def cadastrar(self):
        pass

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def cor(self):
        return self._cor

    @property
    def ano(self):
        return self._ano
    
    @marca.setter
    def marca(self, nova_marca):
        self._marca = nova_marca
    
    @modelo.setter
    def modelo(self, novo_modelo):
        self._modelo = novo_modelo
    
    @cor.setter
    def cor(self, nova_cor):
       self._cor = nova_cor
    
    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, ano, combustivel):
        super().__init__(marca, modelo, cor, ano)
        self._combustivel = combustivel
    
    
    @property
    def combustivel(self):
        return self._combustivel
    
    def cadastrar(self):
        marca = input('Marca do carro: ')
        modelo = input('Modelo do carro: ')
        cor = input('Cor do carro: ')
        ano = int(input('Ano do carro: '))
        combustivel = input('Tipo de combustível: ')

        Veiculo.veiculos['Carro'][marca] = {
            'Modelo': modelo,
            'Cor': cor,
            'Ano': ano,
            'Combustível': combustivel
        }
        print('Carro cadastrado com sucesso!')
     
class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, ano, tipo):
        super().__init__(marca, modelo, cor, ano)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo

    def cadastrar(self):
        marca = input('Marca da moto: ')
        modelo = input('Modelo da moto: ')
        cor = input('Cor da moto: ')
        ano = int(input('Ano da moto: '))
        tipo_moto = input('Tipo da moto (Esportiva, Custom, etc.): ')
        Veiculo.veiculos['Moto'][marca] = {
            'Modelo': modelo,
            'Cor': cor,
            'Ano': ano,
            'Tipo': tipo_moto
        }
        print('Moto cadastrada com sucesso!')

class Caminhao(Veiculo):   
    def __init__(self, marca, modelo, cor, ano, carga):
        super().__init__(marca, modelo, cor, ano)
        self._carga = carga

    @property
    def carga(self):
        return self._carga
    
    @carga.setter
    def carga(self, nova_carga):
        self._carga = nova_carga

    def cadastrar(self):
        marca = input('Marca do caminhão: ')
        modelo = input('Modelo do caminhão: ')
        cor = input('Cor do caminhão: ')
        ano = int(input('Ano do caminhão: '))
        carga_maxima = input('Capacidade de carga (kg): ')
        
        Veiculo.veiculos['Caminhão'][marca] = {
            'Modelo': modelo,
            'Cor': cor,
            'Ano': ano,
            'Carga máxima': carga_maxima
        }
        print('Caminhão cadastrado com sucesso!')          

os.system('cls')

while True:
    print('1. Carro\n2. Moto\n3. Caminhão\n4. Exibir\n5. Trocar dados\n'
          '6. sair')
    escolha = input('Escolha uma opção: ')
    os.system('cls')

    if escolha == '6':
        break
    
    elif escolha == '1':
        os.system('cls')
        carro = Carro('','','',0,'')
        carro.cadastrar()
        
    elif escolha == '2':
        os.system('cls')
        moto = Moto('','','',0,'')
        moto.cadastrar()
        
    elif escolha == '3':
        os.system('cls')
        caminhao = Caminhao('','','',0,'')
        caminhao.cadastrar()
        
    elif escolha == '4':
        print('Tipos de veículo: ')
        print('1. Carro\n2. Moto\n3. Caminhão')
        escolha_veiculo = input('Escolha uma das opções: ')

        if escolha_veiculo == '1':
            os.system('cls')
            if Veiculo.veiculos['Carro']:
                for marca, dados in Veiculo.veiculos['Carro'].items():
                    print('-'*70)
                    print(f'Marca: {marca}\nModelo: {dados["Modelo"]}\n'
                        f'Cor: {dados["Cor"]}\nAno: {dados["Ano"]}\n'
                        f'Combustível: {dados["Combustível"]}')
            else:
                print('Nenhum carro cadastrado.')

        elif escolha_veiculo == '2':
            os.system('cls')
            if Veiculo.veiculos['Moto']:
                for marca, dados in Veiculo.veiculos['Moto'].items():
                    print('-'*70)
                    print(f'Marca: {marca}\nModelo: {dados["Modelo"]}\n'
                        f'Cor: {dados["Cor"]}\nAno: {dados["Ano"]}\n'
                        f'Tipo: {dados["Tipo"]}')
            else:
                print('Nenhuma moto cadastrada.')

        elif escolha_veiculo == '3':
            os.system('cls')
            if Veiculo.veiculos['Caminhão']:
                for marca, dados in Veiculo.veiculos['Caminhão'].items():
                    print('-'*70)
                    print(f'Marca: {marca}\nModelo: {dados["Modelo"]}\n'
                        f'Cor: {dados["Cor"]}\nAno: {dados["Ano"]}\n'
                        f'Carga máxima: {dados["Carga máxima"]}')
            else:
                print('Nenhum caminhão cadastrado.')

    else:
        print('Opção inválida, tente novamente!')




    # PARA LEMBRAR
    # PLANEJO FAZER UMA DIVISÃO POR LISTA OU DICIONARIO(no caso do carro, vai fazer checagem por combustivel,
    # na moto por tipo e no caminhão pela carga maxima)
    # PRATICAMENTE VAI FAZER UMA CHECAGEM SE JÁ EXISTE, E SE NÃO EXISTIR
    # IRA CRIAR UMA PARTE SÓ PARA ESTE TIPO.
    # EX:
    # COMBUSTIVEL1:             TIPO1:                  CARGA MAX1:
    # CARRO1(DADOS)             MOTO1(DADOS)            CAMINHAO1(DADOS)
    # CARRO2(DADOS)             MOTO2(DADOS)            CAMINHAO2(DADOS)
    
    # COMBUSTIVEL2:             TIPO2:                  CARGA MAX2:
    # CARRO1(DADOS)             MOTO1(DADOS)            CAMINHAO1(DADOS)
    # CARRO2(DADOS)             MOTO2(DADOS)            CAMINHAO02(DADOS)