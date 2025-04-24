"""
DESCRIÇÃO: Algoritmo para criar uma lista com nome e peso, mostrar os mais leves e mais pesadas.
AUTOR: Lucas Matias Fontoura
DATA: 03/04/2025
VERSÃO:
(03/04/2025)1.0 -> código, porem com um comentario de ilustração  
(23/04/2025)1.1 -> retirada do comentario de ilustração (mais clean)
"""
resposta = 'S'
lista = list()
lista_tot = list()
lista_tot_leve = list()
lista_tot_pesado = list()
leve = None
pesado = None

while True:
    if resposta == 'S':
        lista.append(str(input('digite o seu nome')))
        lista.append(int(input('digite o seu peso')))
        lista_tot.append(lista.copy())
        lista.clear()
    elif resposta == 'N':
        break
    else:
        print('digite corretamente se deseja continuar ou parar')
    resposta = str(input('digite se deseja continuar [s/n]')).upper().strip()[0]
    
print(lista_tot)

for cont in lista_tot:
    if leve == None:
        leve = cont[1]
        lista_tot_leve.append(cont[0])
    elif leve > cont[1]:
        leve = cont[1]
        lista_tot_leve.clear()
        lista_tot_leve.append(cont[0])
    elif leve == cont[1]:
        lista_tot_leve.append(cont[0])
    if pesado == None:
        pesado = cont[1]
        lista_tot_pesado.append(cont[0])
    elif pesado < cont[1]:
        pesado = cont[1]
        lista_tot_pesado.clear()
        lista_tot_pesado.append(cont[0])
    elif pesado == cont[1]:
        lista_tot_pesado.append(cont[0])
        
print(f'a quantidade total de pessoas na lista é {len(lista_tot)}')
print(f'o peso mais pesado foi de {pesado} com as pessoas:{lista_tot_pesado}')
print(f'o peso mais leve foi de {leve} com as pessoas:{lista_tot_leve}')  