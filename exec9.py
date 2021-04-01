# 9. Reverso do número. Faça uma função que retorne o reverso
# de um número inteiro informado. Por exemplo: 127 -> 721.


def reversao(num):
    reverso = str(num)
    print(f'{num} --> {str(reverso[::-1])} ')


num = int(input('Digite um número inteiro:  '))


reversao(num)
