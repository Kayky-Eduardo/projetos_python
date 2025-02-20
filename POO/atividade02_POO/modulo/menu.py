import os
from modulo.classes import Carro
from modulo.classes import Moto
from modulo.classes import Caminhao

def exibir_menu():
    """Função para criar um menu com opções interativas podendo selecionar
      a opção de cadastrar, exibir, trocar dados e sair"""
    while True:
        print('1. Cadastrar\n2. Exibir\n3. Trocar dados\n'
            '4. sair')
        print('='*70)
        escolha = input('Escolha uma opção: ')
        os.system('cls')

        if escolha == '4':
            break
        
        elif escolha == '1':
            print('1. Carro\n2. Moto\n3. Caminhão')
            print('='*70)
            escolha_veiculo = input('Escolha uma das opções: ')
            
            if escolha_veiculo == '1':
                os.system('cls')
                carro = Carro('','','',0,'')
                carro.cadastrar()
                print('='*70)
                
            if escolha_veiculo == '2':
                os.system('cls')
                moto = Moto('','','',0,'')
                moto.cadastrar()
                print('='*70)
                
            if escolha_veiculo == '3':
                os.system('cls')
                caminhao = Caminhao('','','',0,'')
                caminhao.cadastrar()
                print('='*70)

            else:
                print(f'Opção inválida.')
                
        elif escolha == '2':
            print('='*70)
            print('1. Carro\n2. Moto\n3. Caminhão')
            escolha_veiculo = input('Escolha uma das opções: ')

            if escolha_veiculo == '1':
                os.system('cls')
                Carro.exibir_dados()

            elif escolha_veiculo == '2':
                Moto.exibir_dados()

            elif escolha_veiculo == '3':
                Caminhao.exibir_dados()

        elif escolha == '3':
            print('='*70)
            print('1. Carro\n2. Moto\n3. Caminhão')
            escolha_veiculo = input('Escolha uma das opções: ')

            if escolha_veiculo == '1':
                Carro.trocar_dados()

            elif escolha_veiculo == '2':
                Moto.trocar_dados()


            elif escolha_veiculo == '3':
                Caminhao.trocar_dados()

        else:
            print('Opção inválida, tente novamente!')