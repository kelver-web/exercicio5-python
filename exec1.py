# 1. Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba
# um valor n inteiro e imprima até a n-ésima linha.


def imprime_numeros(n):
    for i in range(n + 1):
        lista = ' '
        for k in range(i):
            lista += str(i) + '\t'
        print(lista)


n = int(input('Digite un número: '))


imprime_numeros(n)
