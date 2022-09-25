from random import shuffle #importa de ran o shu

def embaralhar_as_palavras(coisa):  #apenas funciona quando invocamos a funcao
    a = list(coisa) #ARMAZENA A LISTA NA VARIAVEL A
    shuffle(a)  #embaralha A (lista)
    #deixar o a com join vazio se nao dara espaco entre os itens, letra
    a = "".join(a)  #todos os itens da lista se tornam strings, e podem ser separados pelo valor dentro das aspas
    print(a.upper()) #imrpime tudo em maiuscula

variavel_de_entrada = input("DIGITE UMA PALAVRA: ") #deve ser declarado antes de invocar a def
embaralhar_as_palavras(variavel_de_entrada) #nao conseguimos invocar variaveis que nao existem
