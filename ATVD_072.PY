"""
DESCRIÇÃO: Script para mostrar o numero extenso de 0 ate 20.
AUTOR: Lucas Matias Fontoura
DATA: 26/03/2025
VERSÃO: 1.0
"""
while True:
    tupla = ('zero','um','dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
    cont = int(input("digite um número desejado de 0 até 20 (contando20): "))
    if cont > 20 or cont < 0 :
        print("numero digitado invalido, digite novamente um numero valido.")
    else:
        print(tupla[cont])
        break

