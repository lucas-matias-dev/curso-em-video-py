"""
DESCRIÇÃO: Algoritmo para.
AUTOR: Lucas Matias Fontoura
DATA: 09/04/2025
VERSÃO: 1.0
"""
idade_tot = int()
resposta = 'S'
dicio = dict()
lista = list()
lista_F = list()
lista_acima = list()

while resposta != 'N':
    dicio['nome'] = str(input('digite o seu nome: '))
    dicio['sexo'] = str(input('digite o seu sexo: ')).upper().strip()[0]
    dicio['idade'] = int(input('digite a sua idade: '))
    lista.append(dicio.copy())
    idade_tot += dicio['idade']
    
    if dicio['sexo'] == 'F':
        lista_F.append(dicio.copy())
        
    resposta = str(input('digite se deseja continuar ou parar [S/N]: ')).upper().strip()[0]
    dicio.clear()
    
for k in lista:
    for keys, valor in k.items():
        if keys == 'idade':
            if valor > idade_tot/len(lista):
                lista_acima.append(k['nome'])

print(f'a quantidade de pessoas cadastradas é {len(lista)}')
print(f'a media de idade é {idade_tot/len(lista):5.1f}')
print(f'uma lista com todas as mulheres {lista_F}')
print(f'pessoas com mais da idade media são {lista_acima}')




 