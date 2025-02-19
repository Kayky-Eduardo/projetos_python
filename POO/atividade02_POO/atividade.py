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
    def __init__(self, marca, modelo, cor, ano):
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._ano = ano
        self.veiculos = {'Carro': {}, 'Moto': {}, 'Caminhão': {}}

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
        
    def receber_dados():
        print('Dados para cadastro: ')
        marca = input('Digite a marca do veículo: ')
        modelo = input('Digte o modelo do veículo: ')
        cor = input('Digite a cor do veículo: ')
        ano = int(input(f'Digite o ano de lançamento do veículo: '))
        combustivel = input('Digite o combustivel sendo utilizado: ')
        
        return marca, modelo, cor, ano, combustivel
    
    def adicionar_no_dicionario(self):
        marca, modelo, cor, ano, combustivel = Carro.receber_dados()
        carro = Carro(marca, modelo, cor, ano, combustivel)
        self.veiculos['Carro'][marca] = {
            'Modelo': modelo,
            'Cor': cor,
            'Ano': ano,
            'Combustivel': combustivel
        }
        return carro


    @property
    def combustivel(self):
        return self._combustivel
    
    @combustivel.setter
    def combustivel(self, combustivel):
        self._combustivel = combustivel


class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, ano, tipo):
        super().__init__(marca, modelo, cor, ano)
        self.tipo = tipo

    @property
    def tipo(self):
        return self.tipo
    
    @tipo.setter
    def tipo(self, novo_tipo):
        self.tipo = novo_tipo

    def cadastrar():
        print('Dados para cadastro: ')
        marca = input('Digite a marca do veículo: ')
        modelo = input('Digte o modelo do veículo: ')
        cor = input('Digite a cor do veículo: ')
        ano = int(input(f'Digite o ano de lançamento do veículo: '))
        tipo_moto = input('Digite o combustivel sendo utilizado: ')
        moto = Moto(marca, modelo, cor, ano, tipo_moto)
        return marca, modelo, cor, ano, tipo_moto, moto
             
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

    def cadastrar():
        print('Dados para cadastro: ')
        marca = input('Digite a marca do veículo: ')
        modelo = input('Digte o modelo do veículo: ')
        cor = input('Digite a cor do veículo: ')
        ano = int(input(f'Digite o ano de lançamento do veículo: '))
        carga_maxima = input('Digite o combustivel sendo utilizado: ')
        moto = Moto(marca, modelo, cor, ano, carga_maxima)
        return marca, modelo, cor, ano, carga_maxima, moto
             

os.system('cls')

while True:
    print('1. Carro\n2. Moto\n3. Caminhão\n4. Exibir\n5. Trocar dados\n'
          '6. sair')
    escolha = input('Escolha uma opção: ')
    os.system('cls')

    if escolha == '6':
        break
    
    elif escolha == '1':
        carro = Carro.adicionar_no_dicionario()

    elif escolha == '2':
        marca, modelo, cor, ano, tipo_moto, moto = Moto.cadastrar()
        moto = Moto(marca, modelo, cor, ano, tipo_moto)
        moto.veiculos['Moto'][marca] = {
            'Modelo': modelo,
            'Cor': cor,
            'Ano': ano,
            'Tipo': tipo_moto
            }
        print('Moto cadastrada')
    
    elif escolha == '3':
        marca, modelo, cor, ano, carga_maxima, caminhao  = Moto.cadastrar()
        caminhao.veiculos['Caminhão'][marca] = {
            'Modelo': modelo,
            'Cor': cor,
            'Ano': ano,
            'Carga_maxima': carga_maxima
            }
        print('Caminhão cadastrado')
    
    elif escolha == '4':
        print('Tipos de veículo: ')
        print('1. Carro\n2. Moto\n3. Caminhão')
        escolha_veiculo = input('Escolha uma das opções: ')

        if escolha_veiculo == '1':
            os.system('cls')
            if carro.veiculos['Carro']:
                for veiculo, dados in carro.veiculos['Carro'].items():
                    print('-'*70)
                    print(f'Veículo: {veiculo}\nDados: {dados}')
                        # f'modelo: {dados["modelo"]}\n cor: {dados["cor"]}\n'
                        # f'Ano de lançamento: {dados["ano"]}'
                        # f'\nCombustível: {dados["Combustível"]}')
            else:
                print('Não possuimos nada cadastrados.')
        
        elif escolha_veiculo == '2':
            if moto.veiculos['Moto']:
                for veiculo, dados in moto.veiculos['Moto'].items():
                    print('-'*70)
                    print(f'Veículo: {veiculo}\nmarca: {dados["Marca"]}\n'
                        f'modelo: {dados["modelo"]}\n cor: {dados["cor"]}\n'
                        f'Ano de lançamento: {dados["ano"]}'
                        f'\nTipo: {dados["Tipo"]}')
            else:
                print('Não possuimos nada cadastrados.')

        elif escolha_veiculo == '3':
            if caminhao.veiculos['Caminhão']:
                for veiculo, dados in caminhao.veiculos['Caminhão'].items():
                    print('-'*70)
                    print(f'Veículo: {veiculo}\nmarca: {dados["Marca"]}\n'
                        f'modelo: {dados["modelo"]}\n cor: {dados["cor"]}\n'
                        f'Ano de lançamento: {dados["ano"]}'
                        f'\nCarga máxima: {dados["Carga_maxima"]}')
            else:
                print('Não tem nada cadastrados.')
    
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