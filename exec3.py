# 3. Faça um programa, com uma função que necessite de três argumentos,
# e que forneça a soma desses três argumentos.


def soma(a, b, c):
    return a + b + c


a = int(input('Digite um número:  '))
b = int(input('Digite outro:  '))
c = int(input('Digite outro:  '))


print(f'A soma dos números é = {soma(a, b, c)}')
