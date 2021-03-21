import sys 
from collections import deque

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
		if tabuleiro[coord] != jogador and tabuleiro[coord] != '.':
			posicao_diagonal_princ = checa_diagonal_principal(jogador, adversario, tabuleiro, coord)
			if(posicao_diagonal_princ != None):
				possiveis_posicoes.append(posicao_diagonal_princ)
			posicao_diagonal_sec = checa_diagonal_secundaria(jogador, adversario, tabuleiro, coord)
			if(posicao_diagonal_sec != None):
				possiveis_posicoes.append(posicao_diagonal_sec)
			posicao_vertical = checa_linha_vertical(jogador, adversario, tabuleiro, coord)
			if(posicao_vertical != None):
				possiveis_posicoes.append(posicao_vertical)
			posicao_horizontal = checa_linha_horizontal(jogador, adversario, tabuleiro, coord)
			if(posicao_horizontal != None):
				possiveis_posicoes.append(posicao_horizontal)
	return possiveis_posicoes

# Checa as posições referentes à diagonal principal do adversário a fim de encontrar uma 
# posição válida nela. Retorna a posição caso haja. 
def checa_diagonal_principal(jogador, adversario, tabuleiro, pos_adversario):
	i = 1
	achou_ponto = False
	achou_si_mesmo = False
	coord_x_adv = pos_adversario[0]
	coord_y_adv = pos_adversario[1]

	# Checando a parte superior da diagonal principal
	while(tabuleiro[coord_x_adv - i, coord_y_adv - i] == adversario):
		if(i < min(coord_x_adv, coord_y_adv)):
			i -= 1
	# Se encontrou um espaço vazio após posições com seu adversário, é necessário checar o outro lado 
	# para descobrir se há uma peça do seu time
	if(tabuleiro[coord_x_adv - i, coord_y_adv - i] == '.'): 
		achou_ponto = True
		coord_possivel = (coord_x_adv - i, coord_y_adv - i)
	# Da mesma forma se ocorrer o contrário, mas precisa checar depois se há um espaço em branco na outra
	# parte da diagonal
	elif(tabuleiro[coord_x_adv - i, coord_y_adv - i] == jogador):
		achou_si_mesmo = True
	else:
		return None

	i = 1
	# Se achou ponto de um lado (espaço vazio), terá que achar a si mesmo do outro para ser válida a 
	# jogada
	if(achou_ponto):
		while(tabuleiro[coord_x_adv + i, coord_y_adv + i] == adversario):
			if(max(coord_x_adv + i + 1, coord_y_adv + i + 1) < 7):
				i += 1
		if(tabuleiro[coord_x_adv + i, coord_y_adv + i] == jogador):
			return coord_possivel
	elif(achou_si_mesmo):
		while(tabuleiro[coord_x_adv + i, coord_y_adv + i] == adversario):
			if(i < min(coord_x_adv, coord_y_adv)):
				i += 1
		if(tabuleiro[coord_x_adv + i, coord_y_adv + i] == '.'):
			coord_possivel = (coord_x_adv + i, coord_y_adv + i)
			return coord_possivel

# Checa as posições referentes à diagonal secundária do adversário a fim de encontrar uma 
# posição válida nela. Retorna a posição caso haja. Senão, retorna vazio.
def checa_diagonal_secundaria(jogador, adversario, tabuleiro, pos_adversario):
	achou_ponto = False
	achou_si_mesmo = False
	coord_x_adv = pos_adversario[0]
	coord_y_adv = pos_adversario[1]

	# Checando a parte superior da diagonal secundária
	x = coord_x_adv + 1
	y = coord_y_adv - 1
	while(tabuleiro[x, y] == adversario):
		if(x < 7 and y > 0):
			x += 1
			y -= 1

	# Se encontrou um espaço vazio após posições com seu adversário, é necessário checar o outro lado 
	# para descobrir se há uma peça do seu time
	if(tabuleiro[x, y] == '.'): 
		achou_ponto = True
		coord_possivel = (x, y)
	# Da mesma forma se ocorrer o contrário, mas precisa checar depois se há um espaço em branco na outra
	# parte da diagonal
	elif(tabuleiro[x, y] == jogador):
		achou_si_mesmo = True
	else:
		return None

	x = coord_x_adv - 1
	y = coord_y_adv + 1
	# Se achou ponto de um lado (espaço vazio), terá que achar a si mesmo do outro para ser válida a 
	# jogada
	if(achou_ponto):
		while(tabuleiro[x, y] == adversario):
			if(x > 0 and y < 7):
				x -= 1
				y += 1
		if(tabuleiro[x, y] == jogador):
			return coord_possivel
	elif(achou_si_mesmo):
		while(tabuleiro[x, y] == adversario):
			if(x > 0 and y < 7):
				x -= 1
				y += 1
		if(tabuleiro[x, y] == '.'):
			coord_possivel = (x, y)
			return coord_possivel

def checa_linha_vertical(jogador, adversario, tabuleiro, pos_adversario):
	achou_ponto = False
	achou_si_mesmo = False
	coord_x_adv = pos_adversario[0]
	coord_y_adv = pos_adversario[1]

	# Checando a parte superior da linha vertical
	x = coord_x_adv
	y = coord_y_adv - 1
	while(tabuleiro[x, y] == adversario):
		if(y > 0):
			y -= 1

	# Se encontrou um espaço vazio após posições com seu adversário, é necessário checar o outro lado 
	# para descobrir se há uma peça do seu time
	if(tabuleiro[x, y] == '.'): 
		achou_ponto = True
		coord_possivel = (x, y)
	# Da mesma forma se ocorrer o contrário, mas precisa checar depois se há um espaço em branco na outra
	# parte da vertical
	elif(tabuleiro[x, y] == jogador):
		achou_si_mesmo = True
	else:
		return None

	y = coord_y_adv + 1
	# Se achou ponto de um lado (espaço vazio), terá que achar a si mesmo do outro para ser válida a 
	# jogada
	if(achou_ponto):
		while(tabuleiro[x, y] == adversario):
			if(y < 7):
				y += 1
		if(tabuleiro[x, y] == jogador):
			return coord_possivel
	elif(achou_si_mesmo):
		while(tabuleiro[x, y] == adversario):
			if(y < 7):
				y += 1
		if(tabuleiro[x, y] == '.'):
			coord_possivel = (x, y)
			return coord_possivel

def checa_linha_horizontal(jogador, adversario, tabuleiro, pos_adversario):
	achou_ponto = False
	achou_si_mesmo = False
	coord_x_adv = pos_adversario[0]
	coord_y_adv = pos_adversario[1]

	# Checando a parte da esquerda da linha horizontal
	x = coord_x_adv - 1
	y = coord_y_adv
	while(tabuleiro[x, y] == adversario):
		if(x > 0):
			x -= 1

	# Se encontrou um espaço vazio após posições com seu adversário, é necessário checar o outro lado 
	# para descobrir se há uma peça do seu time
	if(tabuleiro[x, y] == '.'): 
		achou_ponto = True
		coord_possivel = (x, y)
	# Da mesma forma se ocorrer o contrário, mas precisa checar depois se há um espaço em branco na outra
	# parte da horizontal
	elif(tabuleiro[x, y] == jogador):
		achou_si_mesmo = True
	else:
		return None

	x = coord_x_adv + 1
	# Se achou ponto de um lado (espaço vazio), terá que achar a si mesmo do outro para ser válida a 
	# jogada
	if(achou_ponto):
		while(tabuleiro[x, y] == adversario):
			if(x < 7):
				x += 1
		if(tabuleiro[x, y] == jogador):
			return coord_possivel
	elif(achou_si_mesmo):
		while(tabuleiro[x, y] == adversario):
			if(x < 7):
				x += 1
		if(tabuleiro[x, y] == '.'):
			coord_possivel = (x, y)
			return coord_possivel

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



if __name__ == '__main__':
	main()