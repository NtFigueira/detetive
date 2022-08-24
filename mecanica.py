from anotacoes import ordem, livros, ler_lista_nomes


#Mecanica Entrada
def porta():
    pista1 = input("Insira a senha:")
    a = pista1.__contains__("a")
    b = pista1.isspace()
    c = pista1.isnumeric()
    d = pista1.isalpha()
    e = pista1.isalnum()
    f = pista1.isupper()
    g = pista1.islower()
    h = pista1.istitle()
    pista1Gabarito = [a, b, c, d, e, f, g, h]
    pistaResposta = [True, False, False, True, True, False, False, True]
    respostaPositiva1 = "Rosa"
    respostaNegativa1 = "Que Pena"
    if pista1Gabarito == pistaResposta:
        print(respostaPositiva1)
        salaPrincipal()
    else:
        print(respostaNegativa1)
        porta()


def salaPrincipal():
    salas = input("escolha uma sala de 1 a 6:")
    if salas == "1":
        print("Bem vindo a sala 1")
        print("Esta sala está uma bagunça, os livros estão todos misturados. Precisamos devolver os livros e quem sabe achamos uma pista.")
        print("organize em ordem crescente")
        print( "17,85,93,54,47,68,81,40,11,25,39,")
        biblioteca()
    if salas == "2":
        escritorio()
    else:
        salaPrincipal()

def computer():
    pass
    computerSenha = input("Insira o número para descobrir o livro que falta: ")
    if computerSenha == "47":
       print("O morro dos ventos Uivantes")
       print("Achamos, agora vamos para outra sala")
       salaPrincipal()
    else:
        print("Tente denovo")
        computer()

#Mecanica SALA 1  -- ARRAY
registro = [11, 17, 25, 39, 40,47, 54, 68, 76, 81, 93]
desafio1 = [11, 17, 25, 39, 40, 54, 68, 76, 81, 93]
def biblioteca():
    registro = "11, 17, 25, 39, 40, 47, 54, 68, 76, 81, 93"
    desafio1 = livros.sort()
    if ordem == desafio1:
        print("Aqui está o registro: " + registro)
        computer()
    else:
        print("a ordem não está correta")
        voltarSalaPrincipal = input("Voltar a sala Principal?[s/n]")
        if voltarSalaPrincipal == "s":
            salaPrincipal()
        if voltarSalaPrincipal == "n":
            biblioteca()
        else:
            print("Digite n ou n ")
            voltarSalaPrincipal


def lupa():
    qual_nome = input("Algum nome te chamou atenção?")
    if qual_nome == "Emily Bronte":
       print("Eu acredito que às vezes são as pessoas que ninguém espera nada que fazem as coisas que ninguém consegue imaginar.")
       print("Acho que acabou por aqui. Vamos voltar ao saguão:")
       salaPrincipal()
    else:
      print("Não desista, pense as vezes a dica pode estar a um livro de distancia")
      lupa()

def escritorio():
    print("O escritório está bem organzidao, não parece que esteja nada fora do lugar.")
    print ("Espera. O computador não foi desligado. O que temos aqui? Olha tem um arquivo enorme! Será que tem algo aqui que possa nos ajudar?")
    ler_lista_nomes()
    lupa()






    print("")
def cozinha():
    pass
    print("Bem vindo a sala 3")
def quartoHospede():
    pass
    print("Bem vindo a sala 4")

def banheiro():
    pass
    print("Bem vindo a sala 5")

def jardimInverno():
    pass
    print("Bem vindo a sala 6")





# print(pista1Gabarito)
