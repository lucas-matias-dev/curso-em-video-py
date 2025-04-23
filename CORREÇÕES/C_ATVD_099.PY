"""
DESCRIÇÃO: função para obter o maior numero 
AUTOR: Lucas Matias Fontoura
DATA: 19/04/2025
VERSÃO: 1.1 -> erro de interpetação do problema, era para entrar varios valores em uma função e obter o maior valor, isso tudo na função 
(fiz separadamente) 
1.2 -> na verdade não mudou muita coisa, estava certo
"""

def maior (* num):
    maior_num = 0
    for cont in num:
        if maior_num == 0:
            maior_num = cont
        elif maior_num < cont:
            maior_num = cont
    print(f'o maior numero é {maior_num}')  
    
    
maior(2,9,4,5,7,1)