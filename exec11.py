# 11. Data com mês por extenso. Construa uma função que receba
# uma data no formato DD/MM/AAAA e devolva uma string no formato
# D de mesPorExtenso de AAAA. Opcionalmente, valide a data e
# retorne NULL caso a data seja inválida


listagem = [['', 'um', 'dois', 'três', 'quatro', 'cinco',
              'seis', 'sete', 'oito', 'nove', 'dez',
              'onze', 'doze', 'treze', 'quatorze', 'quinze',
              'dezesseis', 'dezessete', 'dezoito', 'dezenove', ],
            ['', 'vinte', 'trinta'], ['janeiro', 'fevereiro',
            'março', 'abril', 'maio', 'junho', 'julho',
            'agosto', 'setembro', 'outubro', 'novembro',
            'dezembro']]

data = input('Digite a data no formato DD/MM/AA: ')
while data[2] != '/' and data[5] != '/' and len(data) != 10:
    print('Data invlálida!')
    data = str(input('Digite a data no formato DD/MM/AA: '))
lista_inteiros = list(map(int, data.split('/')))


def transformador(dia_mes_ano, lista_data):
    
    if lista_data[0] < 20:
        print(dia_mes_ano[0][lista_data[0]], end=' de ')
    else:
        dezena = str(lista_data[0])
        dezena = int(dezena[0])
        print(dia_mes_ano[1][dezena-1], end='')
        unidade = str(lista_data[0])
        unidade = int(unidade[1])
        if unidade == 0:
            print(end=' de ')
        else:
            print(" e", dia_mes_ano[0][unidade], end=' de ')
    mes = str(lista_data[1])

    if mes[0] == '1':
        mes = int(mes[0] + mes[1])
        print(dia_mes_ano[2][mes - 1], end=' de ')
    else:
        mes = int(mes[0])
        print(dia_mes_ano[2][mes - 1], end=' de ')
    print(lista_data[2])


transformador(listagem, lista_inteiros)
