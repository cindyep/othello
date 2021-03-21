import sys 
from collections import deque
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

def busca_possiveis_posicoes(jogador, adversario, tabuleiro):
	possiveis_posicoes = deque()
	for coord in tabuleiro:
		if tabuleiro[coord] == adversario:
			posicao_diagonal_princ = checa_diagonal_principal(jogador, tabuleiro, coord)
			if(posicao_diagonal_princ != None):
				possiveis_posicoes.append(posicao_diagonal_princ)
			posicao_diagonal_sec = checa_diagonal_secundaria(jogador, tabuleiro, coord)
			if(posicao_diagonal_sec != None):
				possiveis_posicoes.append(posicao_diagonal_sec)
			posicao_vertical = checa_linha_vertical(jogador, tabuleiro, coord)
			if(posicao_vertical != None):
				possiveis_posicoes.append(posicao_vertical)
			posicao_horizontal = checa_linha_horizontal(jogador, tabuleiro, coord)
			if(posicao_horizontal != None):
				possiveis_posicoes.append(posicao_horizontal)
	return possiveis_posicoes

# Checa as posições referentes à diagonal principal do adversário a fim de encontrar uma 
# posição válida nela. Retorna a posição caso haja. 
def checa_diagonal_principal(jogador, tabuleiro, pos_adversario):
	peca_encontrada_1, (coord_x_1, coord_y_1) = busca_pecas(tabuleiro, jogador, pos_adversario, -1, -1)
	if(peca_encontrada_1 == jogador):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, +1, +1)
		if(peca_encontrada_2 == '.'):
			return (coord_x_2, coord_y_2)
	elif(peca_encontrada_1 == '.'):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, +1, +1)
		if(peca_encontrada_2 == jogador):
			return (coord_x_1, coord_y_1)
	else:
		return None

# Checa as posições referentes à diagonal secundária do adversário a fim de encontrar uma 
# posição válida nela. Retorna a posição caso haja. Senão, retorna vazio.
def checa_diagonal_secundaria(jogador, tabuleiro, pos_adversario):
	peca_encontrada_1, (coord_x_1, coord_y_1) = busca_pecas(tabuleiro, jogador, pos_adversario, +1, -1)
	if(peca_encontrada_1 == jogador):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, -1, +1)
		if(peca_encontrada_2 == '.'):
			return (coord_x_2, coord_y_2)
	elif(peca_encontrada_1 == '.'):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, -1, +1)
		if(peca_encontrada_2 == jogador):
			return (coord_x_1, coord_y_1)
	else:
		return None

def checa_linha_horizontal(jogador, tabuleiro, pos_adversario):
	peca_encontrada_1, (coord_x_1, coord_y_1) = busca_pecas(tabuleiro, jogador, pos_adversario, -1, 0)
	if(peca_encontrada_1 == jogador):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, +1, 0)
		if(peca_encontrada_2 == '.'):
			return (coord_x_2, coord_y_2)
	elif(peca_encontrada_1 == '.'):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, +1, 0)
		if(peca_encontrada_2 == jogador):
			return (coord_x_1, coord_y_1)
	else:
		return None

def checa_linha_vertical(jogador, tabuleiro, pos_adversario):
	peca_encontrada_1, (coord_x_1, coord_y_1) = busca_pecas(tabuleiro, jogador, pos_adversario, 0, -1)
	if(peca_encontrada_1 == jogador):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, 0, +1)
		if(peca_encontrada_2 == '.'):
			return (coord_x_2, coord_y_2)
	elif(peca_encontrada_1 == '.'):
		peca_encontrada_2, (coord_x_2, coord_y_2) = busca_pecas(tabuleiro, jogador, pos_adversario, 0, +1)
		if(peca_encontrada_2 == jogador):
			return (coord_x_1, coord_y_1)
	else:
		return None

# Busca as peças de sua inicial e '.', movendo as coord x e y conforme especificado
# Retorna tupla com peça encontrada e as coordenadas dela
def busca_pecas(tabuleiro, jogador, pos_adversario, move_dir_x, move_dir_y):
	achou_ponto = False
	achou_si_mesmo = False
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

def main():
	tabuleiro = {}

	arquivo_de_estado = sys.argv[1]
	nome_jogador = sys.argv[2]
	jogador = nome_jogador[0].upper()

	tabuleiro = le_arquivo_e_atualiza_tabuleiro(arquivo_de_estado, tabuleiro)
	print(tabuleiro)
	adversario = devolve_adversario(jogador)
	possiveis_posicoes = busca_possiveis_posicoes(jogador, adversario, tabuleiro)
	print(possiveis_posicoes)
	print(conta_pecas(jogador, tabuleiro))



if __name__ == '__main__':
	main()