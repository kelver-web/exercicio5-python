# 7. Faça um programa que use a função valorPagamento para determinar
# o valor a ser pago por uma prestação de uma conta. O programa deverá
# solicitar ao usuário o valor da prestação e o número de dias em atraso
# e passar estes valores para a função valorPagamento, que calculará o
# valor a ser pago e devolverá este valor ao programa que a chamou.
# O programa deverá então exibir o valor a ser pago na tela. Após a
# execução o programa deverá voltar a pedir outro valor de prestação e
# assim continuar até que seja informado um valor igual a zero para a
# prestação. Neste momento o programa deverá ser encerrado, exibindo o
# relatório do dia, que conterá a quantidade e o valor total de prestações
# pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma.
# Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver
# atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.


def valor_pagamento(valor_prestacao, dias_atrasados):
    if dias_atrasados == 0:
        valor = valor_prestacao
        return valor

    else:
        valor = (valor_prestacao * 1.03) * ((0.001 * dias_atrasados) + 1)
        return valor


relatorio = []
valor_prestacao = True
prestacoes = []

while valor_prestacao != 0:
    valor_prestacao = float(input('\nDigite o valor da prestação:  '))
    if valor_prestacao == 0:
        break
    else:
        dias_atrasados = int(input('Dias em atraso:  '))
        valor = valor_pagamento(valor_prestacao, dias_atrasados)
        relatorio.append(valor)
        prestacoes.append(valor_prestacao)
        soma = sum(relatorio)

print()
print('===== *** RELATÓRIO DO DIA *** =====')
print('Quant. Prestações:               Valor com juros:')

for i in range(len(relatorio)):
    print(f'{i + 1}º Prestação R$ {prestacoes[i]:.0f} ----------- R$ {relatorio[i]:.0f}')
print(f'Total --------------------------- R$ {soma:.0f}')
