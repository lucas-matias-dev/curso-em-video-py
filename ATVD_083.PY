"""
DESCRIÇÃO: Script para validar expressões matematicas.
AUTOR: Lucas Matias Fontoura
DATA: 1/04/2025
VERSÃO: 
(01/04/2025)1.0 ->  formato 1
(01/04/2025)1.1 -> formato 2
(23/04/2025)1.2 -> formato 1 em comentario e correção de descrição
"""
#versão 1: essa versão consiste em um formato diferente do pedido (usando string)
#é um modo bem mais simples, porem, não é o pedido
"""
expressao = str(input('digite a sua expressão matematica para aferir se é valida'))
if expressao.count(')') == 1 and expressao.count('('):
    print('sua expressão é valida')
elif expressao.count('(')%2 == 0 and expressao.count(')')%2 == 0:
    print('sua expressão é valida')
else:
    print('sua expressão é invalida') 
"""

#versão 1.1: essa versão consiste no formato pedido no exercicio (lista):    
lista = list()
lista.append(str(input('digite sua expressão matematica')))
if lista.count('(') == 1 and lista.count(')'):
    print('expressão valida')
elif lista.count('(')%2 == 0 and lista.count(')')%2 == 0:
    print('expressão valida')
else:
    print('expressão invalida.')    