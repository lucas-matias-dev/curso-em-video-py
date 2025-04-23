"""
DESCRIÇÃO: Algoritmo para gerenciar aproveitamento de jogadores.
AUTOR: Lucas Matias Fontoura
DATA: 09/04/2025
VERSÃO: 1.0
"""

tot_gols = gol = cont2 = 0
resposta = 'S'
gols = list()
jogadores = list()
jogador = dict()

while resposta != 'N':
    
    jogador['nome'] = str(input('digite o nome do jogador: '))
    jogador['partidas'] = int(input('digite a quantidade de partidas: '))

    for partida in range(0,jogador['partidas']):
        gol = int(input(f'digite a quantidade de gols na partida {partida}:'))
        gols.append(gol)
        tot_gols += gol

    jogador['gols'] = gols.copy()
    jogador['total'] = tot_gols
    
    jogadores.append(jogador.copy())
    
    jogador.clear()
    tot_gols = 0
    gols.clear()
    
    resposta = str(input('deseja continuar?[S/N]'))
    
print('')
print(f'{"N°":<5}{"Nome":<15}{"Partidas":<10}{"Gols":<20}{"Total"}')
print('-' * 70)

for idx, cont in enumerate(jogadores):
    gols_str = str(cont['gols'])  # transforma a lista de gols em string pra imprimir
    print(f'{idx:<5}{cont["nome"]:<15}{cont["partidas"]:<10}{gols_str:<20}{cont["total"]}')
