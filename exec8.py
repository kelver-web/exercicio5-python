# 8. Faça uma função que informe a quantidade de dígitos de um
# determinado número inteiro informado.


def informa_digito(num):
    digito = str(num)
    print(f'Quantidade de dígitos:  {len(digito)}')


num = int(input('Digite um número inteiro: '))
informa_digito(num)
