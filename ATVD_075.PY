"""
DESCRIÇÃO: Script gerar 5 numeros aleatorios e colocar em uma tupla.
AUTOR: Lucas Matias Fontoura
DATA: 26/03/2025
VERSÃO: 1.0
"""
tupla_perm = tuple()
tupla_par = tuple()

for cont in range (0,4):
    num = int(input("digite um numero"))
    if num%2 == 0:
        tupla_par = tupla_par+ (num,)
    tupla_temp = (num,)
    tupla_perm = tupla_temp + tupla_perm
    del(tupla_temp)
    
print(tupla_perm)
if 9 in tupla_perm:
    print(f"na tupla {tupla_perm}possui {tupla_perm.count(9)} noves")
else:
    print(f"na tupla {tupla_perm} não possui 9")
if 3 in tupla_perm:
    print(f"o primeiro valor 3 foi digitado em {tupla_perm.index(3)}")
else:
    print(f"na tupla {tupla_perm} não possui 3")     
print(f"os numeros pares foram {tupla_par}")
    
    