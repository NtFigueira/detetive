import pandas as pd
from openpyxl import *


#__Abrindo a porta da mansão:
# Ao se aproximar da porta nos deparamos com um display com a seguinte mensagem:
# Não importa quem sou, desde que se siga as regras:
# "a"? = 1 /" " = 0 / 123 = 0 / abc = 1 / abc123 = 0 / A = 0/ a = 0 / Aa = 1


# Entrando na mansão é possivel ver 4 portas e um elevador a frente.#
# Parece que o elevador está parado no segundo andar. E não parece possível chama-lo sem um novo código#
# Vamos ver se encontramos algo nas salas.#

#__Sala 1 :
# insira seu código aqui:

livros = [68,40,93,11,76,18,39,54,81,25]
ordem = livros.sort()

## Sala 2 :
#insira seu código aqui:

#documento = pd.read_csv("lista_pessoas.csv")
#def ler_lista_nomes():
#    with open("lista_pessoas.csv", "r", encoding ="UTF-8") as documento:
#        for nome in documento:
#            if "Emily Bronte" in nome:
#                print(nome)


### Sala 3:
#Insira seu código aqui:

listagem = pd.read_excel('intruso.xlsx', sheet_name='Panddington', usecols=["Alan",'Turing'])
def ler_listagem():
    print(listagem.loc[41])
ler_listagem()
def Intruso():



