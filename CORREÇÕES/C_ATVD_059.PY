"""
DESCRIÇÃO: Script para calculadora.
AUTOR: Lucas Matias Fontoura
DATA: 21/03/2025
VERSÃO: 1.0
"""
from time import sleep
n1 = int(input('digite o primeiro número'))
n2 = int(input('digite o segundo número'))
opcao = 0

while opcao != 5:
    print("""|============MENU============|     
|       1 - somar            |
|       2 - multiplicar      |
|       3 - maior            |
|       4 - novos números    |
|       5 - sair do programa |
|============================|""")
    opcao = int (input('digite opção desejada:'))
    if opcao == 1:
        print('a soma entre os números é {}'.format(n1+n2))
    elif opcao == 2:
        print('a multiplicação entre os números é {}'.format(n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('o numero {} é maior que {}'.format(n1,n2))
        elif n2 > n1:
            print('o número {} é maior que {}'.format(n2,n1))
        else:
            print('os numeros são iguais')
    elif opcao == 4:
        n1 = int(input('digite o primeiro número'))
        n2 = int(input('digite o segundo número'))   
    elif opcao > 5 or opcao < 0:
        print('opção invalido')
    sleep(2)
print('programa finalizado')