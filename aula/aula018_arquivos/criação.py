# Importar a biblioteca csv
import os
import csv

# Criando uma lista de dicionários: cada dicionário é uma linha (registro)
lista = [
    {'nome':'Agata', 'telefone': '(32)99196-0000', 'cidade':'Juiz de Fora'},
    {'nome':'Bia', 'telefone': '(32)99196-1111', 'cidade': 'Juiz de fora'},
    {'nome':'Coly', 'telefone': '(32)99196-2222', 'cidade': 'Juiz de fora'},
    {'nome':'Isis', 'telefone': '(32)99196-3333', 'cidade': 'Juiz de fora'}
]

# Caminho para a pasta onde o arquivo CSV será salvo
pasta = 'arquivos_cvs/gravacao/'

# Verificando se a pasta existe, se não irá criá-la
os.makedirs(pasta, exist_ok=True)

# nome para o arquivo CSV para gravar as informações
arquivo = 'arquivos_cvs/gravacao/alunas.csv'

# Caminho completo do arquivo CSV
caminho_arquivo = os.path.join(pasta, arquivo)

#Abre o arquivo 'arquivo' no modo de escrita ('w').
# Se o arquivo não existir, ele será criado; se existir, sera truncado (esvaziado).
# newline='': Evita a adição de linhas em branco extras ao gravar o arquivo em algumas plataformas.
# as arquivo_csv: Atribui o objeto arquivo ao 'arquivo_csv' para ser usado dentro do bloco with.
with open(arquivo, 'w', newline='') as arquivo_csv:

    # campos = ['name', 'telefone', 'cidade]: Define a lista de nomes de campos
    # (cabeçalhos das colunas do CSV)
    campos = ['nome', 'telefone', 'cidade']

    # writer = csv.DictWriter(arquivo_csv, fieldnames=campos):
    # Cria um objeto DictWriter que usará 'arquivo_csv' para gravar os campos.
    # fieldnames define a ordem dos campos no arquivo CSV.
    # delimeter=';': é o separador
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')

    # writer.writeheader(): Grava a linha de cabeçalho no
    # arquivo CSV usando os nomes de campos definidos em fieldnames.
    escrever.writeheader()

    # write.writerows(lista): grava todas as linhas da lista no arquivo CSV.
    # Cada dicionário em 'lista' se torna uma linha no arquivo.
    escrever.writerows(lista)

os.system('cls')
# Exibe uma mensagem indicando que o arquivo foi gravado com sucesso.
print(f'Arquivo {arquivo} gravado com sucesso!')