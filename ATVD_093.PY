"""
DESCRIÇÃO: Algoritmo para gerenciar aproveitamento de jogadores.
AUTOR: Lucas Matias Fontoura
DATA: 09/04/2025
VERSÃO: 1.0
"""
tot_gols = 0
gol = 0
gols = []
jogador = {}
jogador['nome'] = str(input('digite o nome do jogador: '))
jogador['partidas'] = int(input('digite a quantidade de partidas: '))

for partida in range(0,jogador['partidas']):
    gol = int(input(f'digite a quantidade de gols na partida {partida}:'))
    gols.append(gol)
    tot_gols += gol

jogador['gols'] = gols
jogador['total'] = tot_gols
print(jogador)

