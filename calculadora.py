#a) Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.
#b) Construa uma função que receba uma string como parâmetro e devolva outra string caracteres embaralhados. 

x = int(input("DIGITE UM VALOR INTEIRO: ")) #declaracao de variavel de entrada inteira
if x > 0: #se x for maior de 0, imprimir a tabuada
    x1 = x * 1
    x2 = x * 2
    x3 = x * 3
    x4 = x * 4
    x5 = x * 5
    x6 = x * 6
    x7 = x * 7
    x8 = x * 8
    x9 = x * 9
    x10 = x * 10
else :
    print("valor inválido!")
print("A TABUADA DO VALOR DIGITADO É: \n" +  str(x2)) #mostrar tabuada
print("A TABUADA DO VALOR DIGITADO É: \n" +  str(x3)) 

