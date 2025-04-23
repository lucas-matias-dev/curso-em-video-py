"""
DESCRIÇÃO: algoritmo para mostrar o numero extenso de 0 ate 20, até que se deseja parar.
AUTOR: Lucas Matias Fontoura
DATA: 27/03/2025
VERSÃO: 1.1, apenas o desafio de colocar em loop até que se deseja parar
"""
desejo = ''
while desejo != "N":
    while True:
        desejo=""
        tupla = ('zero','um','dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
        cont = int(input("digite um número desejado de 0 até 20 (contando20): "))
        if cont > 20 or cont < 0 :
            print("numero digitado invalido, digite novamente um numero valido.")
        else:
            print(tupla[cont])
            break
    while desejo not in ("S","N"):
        desejo = str (input("digite se dejesa continuar ou não [S/N]")).upper().strip()
        if desejo in ("S","N"):
            break
        else:
            print("digite novamente")
        print(desejo)
    
        

