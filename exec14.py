# 14. Quadrado mágico. Um quadrado mágico é aquele dividido em
# linhas e colunas, com um número em cada posição e no qual a
# soma das linhas, colunas e diagonais é a mesma. Por exemplo,
# veja um quadrado mágico de lado 3, com números de 1 a 9:

''' 8  3  4
    1  5  9
    6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos
com as características acima. Dica: produza todas as combinações possíveis e
verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece
ser mais simples que usar uma matriz 3x3.'''

import random

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def quadrado_magico():
    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        print(matriz)


vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]


for i in range(3):
    for k in range(3):
        choice = random.choice(vetor)
        matriz[i][k] = choice
        indice = vetor.index(choice)
        vetor = vetor[:indice] + vetor[indice + 1:]


quadrado_magico()
print(f'\n{matriz[0]} \n{matriz[1]} \n{matriz[2]}')
