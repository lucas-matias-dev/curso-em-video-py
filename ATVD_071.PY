"""
DESCRIÇÃO: Script de caixa de banco.
AUTOR: Lucas Matias Fontoura
DATA: 22/03/2025
VERSÃO: 1.0
"""
valor = int (input('digite o valor que deseja sacar: '))
v1 = v5 = v10 = v20 = v50 = 0
while valor !=0:
    if valor >= 50:
        v50 += 1
        valor -= 50
    elif valor < 50 and valor >= 20:
        v20 += 1
        valor -= 20
    elif valor < 20 and valor >= 10:
        v10 += 1
        valor -= 10
    elif valor < 10 and valor >= 5:
        v5 += 1
        valor -= 5
    elif valor < 5 and valor > 0:
        v1 += 1
        valor -= 1
print(f"""      cedulas de 50 : {v50}
      cedulas de 20: {v20}
      cedulas de 10: {v10}
      cedulas de 5: {v5}
      cedulas de 1: {v1}
      """)
        