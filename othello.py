import sys 
from collections import deque
import copy
from numpy import inf
from minimax import *

def le_arquivo_e_atualiza_tabuleiro(arquivo, tabuleiro):
	x = y = 0	# coordenadas
	with open(arquivo) as arq:
		for linha in arq:
			for ch in linha:
				if(ch != '\n'):
					tabuleiro[(x, y)] = ch
					x += 1
			x = 0
			y += 1
	return tabuleiro

def encontra_acoes_validas(jogador, tabuleiro):
	adversario = devolve_adversario(jogador)
	possiveis_acoes = deque()
	for coord in tabuleiro:
		if tabuleiro[coord] == adversario:
			acao = checa_diagonal_principal(jogador, tabuleiro, coord)
			if(acao != None):
				possiveis_acoes.append(acao)
			acao = checa_diagonal_secundaria(jogador, tabuleiro, coord)
			if(acao != None):
				possiveis_acoes.append(acao)
			acao = checa_linha_vertical(jogador, tabuleiro, coord)
			if(acao != None):
				possiveis_acoes.append(acao)
			acao = checa_linha_horizontal(jogador, tabuleiro, coord)
			if(acao != None):
				possiveis_acoes.append(acao)
	return possiveis_acoes

# Checa as posições referentes à diagonal principal do adversário a fim de encontrar uma 
# posição válida nela. 
# Retorna: posição onde colocar a peça, posição onde está sua outra peça para capturar o oponente.
def checa_diagonal_principal(jogador, tabuleiro, pos_adversario):
	peca_encontrada_1, (coord_x_1, coord_y_1) = busca_pecas(tabuleiro, jogador, pos_adversario, -1, -1)
	if(peca_encontrada_1 == jogador):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, +1, +1)
		if(peca_encontrada_2 == '.'):
			return ((coord_x_2, coord_y_2), (coord_x_1, coord_y_1))
	elif(peca_encontrada_1 == '.'):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, +1, +1)
		if(peca_encontrada_2 == jogador):
			return ((coord_x_1, coord_y_1), (coord_x_2, coord_y_2))
	else:
		return None

# Checa as posições referentes à diagonal secundária do adversário a fim de encontrar uma 
# posição válida nela. Retorna a posição caso haja. Senão, retorna vazio.
def checa_diagonal_secundaria(jogador, tabuleiro, pos_adversario):
	peca_encontrada_1, (coord_x_1, coord_y_1) = busca_pecas(tabuleiro, jogador, pos_adversario, +1, -1)
	if(peca_encontrada_1 == jogador):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, -1, +1)
		if(peca_encontrada_2 == '.'):
			return ((coord_x_2, coord_y_2), (coord_x_1, coord_y_1))
	elif(peca_encontrada_1 == '.'):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, -1, +1)
		if(peca_encontrada_2 == jogador):
			return ((coord_x_1, coord_y_1), (coord_x_2, coord_y_2))
	else:
		return None

def checa_linha_horizontal(jogador, tabuleiro, pos_adversario):
	peca_encontrada_1, (coord_x_1, coord_y_1) = busca_pecas(tabuleiro, jogador, pos_adversario, -1, 0)
	if(peca_encontrada_1 == jogador):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, +1, 0)
		if(peca_encontrada_2 == '.'):
			return ((coord_x_2, coord_y_2), (coord_x_1, coord_y_1))
	elif(peca_encontrada_1 == '.'):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, +1, 0)
		if(peca_encontrada_2 == jogador):
			return ((coord_x_1, coord_y_1), (coord_x_2, coord_y_2))
	else:
		return None

def checa_linha_vertical(jogador, tabuleiro, pos_adversario):
	peca_encontrada_1, (coord_x_1, coord_y_1) = busca_pecas(tabuleiro, jogador, pos_adversario, 0, -1)
	if(peca_encontrada_1 == jogador):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, 0, +1)
		if(peca_encontrada_2 == '.'):
			return ((coord_x_2, coord_y_2), (coord_x_1, coord_y_1))
	elif(peca_encontrada_1 == '.'):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, 0, +1)
		if(peca_encontrada_2 == jogador):
			return ((coord_x_1, coord_y_1), (coord_x_2, coord_y_2))
	else:
		return None

# Busca as peças de sua inicial e '.', movendo as coord x e y conforme especificado
# Retorna tupla com peça encontrada e as coordenadas dela
def busca_pecas(tabuleiro, jogador, pos_adversario, move_dir_x, move_dir_y):
	adversario = devolve_adversario(jogador)
	coord_x_adv = pos_adversario[0]
	coord_y_adv = pos_adversario[1]

	# Checando a parte da esquerda da linha horizontal
	x = coord_x_adv + move_dir_x
	y = coord_y_adv + move_dir_y
	while(tabuleiro[x, y] == adversario):
		if(x > 0 and x < 7 and y > 0 and y < 7):
			x += move_dir_x
			y += move_dir_y

	# Se encontrou um espaço vazio após posições com seu adversário, é necessário checar o outro lado 
	# para descobrir se há uma peça do seu time
	if(tabuleiro[x, y] == '.'): 
		coord_possivel = (x, y)
		return '.', (x, y)
	# Da mesma forma se ocorrer o contrário, mas precisa checar depois se há um espaço em branco na outra
	# parte da horizontal
	elif(tabuleiro[x, y] == jogador):
		return jogador, (x, y)
	else:
		return None

def devolve_adversario(jogador):
	if(jogador == 'B'):
		return 'W'
	else:
		return 'B'

# Calcula o estado do tabuleiro após o jogador coloca a peça na posição especificada.
def calcula_novo_estado(tabuleiro, jogador, acao):
	min_x = acao[0][0]
	min_y = acao[0][1]
	max_x = acao[1][0]
	max_y = acao[1][1]

	tabuleiro_novo = copy.deepcopy(tabuleiro)

	if(min_y > max_y):
		move_y = -1
	elif(min_y < max_y):
		move_y = 1
	else:
		move_y = 0

	if(min_x > max_x):
		move_x = -1
	elif(min_x < max_x):
		move_x = 1
	else:
		move_x = 0

	x = min_x
	y = min_y

	while(x != max_x or y != max_y):
		tabuleiro_novo[x, y] = jogador
		x += move_x
		y += move_y

	return tabuleiro_novo

def imprime_tabuleiro(tabuleiro):
	for y in range(0, 7):
		for x in range(0, 7):
			print(tabuleiro[x, y], end = "")
		print("")

def main():
	grafo = {}
	estado_tabuleiro = {}

	arquivo_de_estado = sys.argv[1]
	nome_jogador = sys.argv[2]
	jogador = nome_jogador[0].upper()

	estado_tabuleiro = le_arquivo_e_atualiza_tabuleiro(arquivo_de_estado, estado_tabuleiro)
	imprime_tabuleiro(estado_tabuleiro)

	#  Nodo(estado, pai, acao, alfa, beta)
	pai = Nodo(estado_tabuleiro, 0, "", inf, -inf)
	grafo[pai] = []
	acoes = encontra_acoes_validas(jogador, estado_tabuleiro)
	alfa = 0
	beta = 0
	#imprime_tabuleiro(novo_tabuleiro)
	for a in acoes:
		novo_tabuleiro = calcula_novo_estado(estado_tabuleiro, jogador, a)
		filho = Nodo(novo_tabuleiro, pai, a[0], alfa, beta)
		grafo[pai].append(filho)
		print("antes:")
		imprime_tabuleiro(estado_tabuleiro)
		filho.imprimeNodo()

if __name__ == '__main__':
	main()