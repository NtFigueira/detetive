from anotacoes import ordem, livros, ler_lista_nomes, senhaCameras, seguranca
import vlc
import pafy
import youtube_dl


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
    salas = input("escolha uma sala de 1 a 4:")
    if salas == "1":
        print("""Bem vindo a sala Biblioteca
            Esta sala está uma bagunça, os livros estão todos misturados. Precisamos devolver os livros e quem sabe achamos uma pista.
            organize em ordem crescente
            17,85,93,54,47,68,81,40,11,25,39,""")
        biblioteca()
    if salas == "2":
        escritorio()
    if salas == "3":
        salaVideo()
    if salas == "4":
        Elevador()
    else:
        salaPrincipal()



#Mecanica biblioteca
def computer():
    computerSenha = input("Insira o número para descobrir o livro que falta: ")
    if computerSenha == "47":
       print("""O morro dos ventos Uivantes"
            Achamos, agora vamos para outra sala""")
       salaPrincipal()
    else:
        print("Tente denovo")
        computer()
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

# Mecanica Escritório
def lupa():
    qual_nome = input("Algum nome te chamou atenção?")
    if qual_nome == "Emily Bronte":
       print("""Eu acredito que às vezes são as pessoas que ninguém espera nada que fazem as coisas que ninguém consegue imaginar.")
             Acho que acabou por aqui. Vamos voltar ao saguão:""")
       salaPrincipal()
    else:
      print("Não desista, pense as vezes a dica pode estar a um livro de distancia")
      lupa()
def escritorio():
    print("""O escritório está bem organzidao, não parece que esteja nada fora do lugar.
        Espera. O computador não foi desligado. O que temos aqui? Olha tem um arquivo enorme! Será que tem algo aqui que possa nos ajudar?""")
    ler_lista_nomes()
    lupa()

#Mecanica Sala de Video
def decisãoSalaVideo():
    pass
    respotaDecisaoSalaVideo = input(
        "Deseja continuar procurando(digite continuar), ou voltar para a sala principal(digite voltar)? ")
    if respotaDecisaoSalaVideo == "continuar":
        salaVideo()
    if respotaDecisaoSalaVideo == "voltar":
        salaPrincipal()
    else:
        print("Precisa decidir corretamente: ")
    decisãoSalaVideo()

def assistirOuVoltar():
        print("Sinto muito.Precisamos decidir")
        decisãoSalaVideo()
def salaVideo():
    print("""O Sr. Coelho adora assistir desenho.Será que conseguiremos achar algo por aqui?
            Olha se reparar cada coluna de dvds tem um nome e um index. Deixa-me ver.
            Essas colunas tem nomes estranhos: Disney, Panddington e Alaska
            Espera, não são nomes de filmes, são personagens.
            Mas que desenho é esse que está passando, parece uma animção. Será que temos um intruso?""")
    studio = input("Qual é o nome do studio? ")
    animacao = input("qual é o nome da animação? ")
    if studio == "Ghibli" and animacao == "O conto da princesa":
         print("Parabens, encontramos!")
         salaPrincipal()
    else:
        assistirOuVoltar()


#Mecanica ELevador

senha = "lobo, Alan Turing, Kaguya"
cam = senhaCameras
camValida = seguranca.replace("coração","fire")


def segundoAndar():
    pass
    print("""Parabéns, conseguimos pegar o Elevador
    Aqui em cima tem várias cameras.
    Talvez consigamos recuperar ver nas gravações quem matou o senhor Toupeira.
    Tem uma frase aqui:
    No coração de um inglês apaixonado, só resta fogo!
    coração on coração""")
    respostaFinal()
def respostaFinal():
    pass
    if senhaCameras== camValida:
        print("Descubra o que aconteceu com o Sr. Coelho:https://www.youtube.com/watch?v=vk_xq1P7vIU")
    else:
        print("Tenta denovo")
        print(cam)
        print(camValida)

def Elevador():
    inserirSenha = input("um animal, uma pessoa e uma princesa:")
    print(senha)
    if inserirSenha == senha:
        segundoAndar()
    else:
        "É preciso o caminho rever"
        salaPrincipal()





