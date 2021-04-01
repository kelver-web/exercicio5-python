# 6. Faça um programa que converta da notação de 24 horas para
# a notação de 12 horas. Por exemplo, o programa deve converter
# 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão
# e uma para a saída. Registre a informação A.M./P.M.
# como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
# efetuar as conversões terá um parâmetro formal para registrar
# se é A.M. ou P.M. Inclua um loop que permita que o usuário repita
# esse cálculo para novos valores de entrada todas as vezes que desejar.


def conversor(hora_24):
    hora_12 = hora_24 - 12
    return hora_12


def saida(hora_12, hora_24, minutos):
    if hora_24 >= 12 and hora_24 <= 24:
        print(f'{hora_12} : {minutos} minutos - PM')
    else:
        print(f'{hora_24} : {minutos} minutos - AM')


while True:
    hora_24 = int(input('\nDigite a hora: '))
    minutos = int(input('Digite o minuto: '))
    hora_12 = conversor(hora_24)
    saida(hora_12, hora_24, minutos)
