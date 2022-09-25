x1 = int(input("DIGITE UM VALOR INTEIRO: ")) #recebe o que o usuario digita e transforma em inteiro/apenas n
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def  executar_lista(itens, valor ): #funcao f(x)
    for tabuada in itens: #exclusivo para lista, checa os elementos da lista e nomeia a posicao
        if valor > 0: 
            print ( str(valor) + " X "+ str(tabuada) + " = "+ str(valor*tabuada))
#criei a funcao com def e agora chamo a funcao 
print("OS NUMEROS DA TABUADA SAO:" )
executar_lista( lista, x1) #passar como parametro, chamando a funcao se utilizando de dois parametros
