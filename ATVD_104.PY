"""
DESCRIÇÃO: função para ler um numero inteiro
AUTOR: Lucas Matias Fontoura
DATA: 11/04/2025
VERSÃO: 1.0
"""
#definição de funções:
def leia_int (n1):
    resposta = n1.isnumeric()
    if resposta == True:
        print('seu numero é inteiro')
        print(f'vc digitou {n1}')
    return resposta

n1 = leia_int('digite um numero')
print(n1)
#programa principal: