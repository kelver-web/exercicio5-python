# 13. Desenha moldura. Construa uma função que desenhe um
# retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas,
# sendo que o valor por omissão é o valor mínimo igual a 1 e o
# valor máximo é 20. Se valores fora da faixa forem informados,
# eles devem ser modificados para valores dentro da faixa de forma elegante.

print('==== MOLDURA RETÂNGULO ====')
altura = int(input('Digite a altura: '))
largura = int(input('Digite a largura: '))

while altura < 1 or altura > 20 or largura < 1 or largura > 20:
    print('Digite numeros entre 1 e 20')
    altura = int(input('Digite a altura: '))
    largura = int(input('Digite a largura: '))


def linhas(largura):
    print('+', '  -  ' * (largura - 2), '+')


def colunas(altura, largura):
    for i in range(altura - 2):
        print('|', '     ' * (largura - 2), '|')


def desenhar(altura, largura):
    linhas(largura)
    colunas(altura, largura)
    linhas(largura)


desenhar(altura, largura)
