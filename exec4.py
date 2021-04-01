# 4. Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento
# for positivo, e ‘N’, se seu argumento for zero ou negativo.

def positivo_ou_negativo(n):
    if n > 0:
        return f'{n} é um número positivo [P]'
    elif n <= 0:
        return f'{n} é um número negativo [N]'


n = int(input('Digite um número:  '))


print(positivo_ou_negativo(n))
