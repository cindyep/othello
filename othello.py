import sys 

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

def busca_possiveis_posicoes(jogador, tabuleiro):
	possiveis_posicoes = []
	for coord in tabuleiro:
		if tabuleiro[coord] != jogador and tabuleiro[coord] != '.':
			if(tabuleiro[(coord[0] - 1, coord[1])] == '.'): # linha horizontal
				possiveis_posicoes.append((coord[0] - 1, coord[1]))
	return possiveis_posicoes

def main():
	tabuleiro = {}

	arquivo_de_estado = sys.argv[1]
	nome_jogador = sys.argv[2]
	jogador = nome_jogador[0].upper()

	tabuleiro = le_arquivo_e_atualiza_tabuleiro(arquivo_de_estado, tabuleiro)
	print(tabuleiro)
	possiveis_posicoes = busca_possiveis_posicoes(jogador, tabuleiro)
	print(possiveis_posicoes)



if __name__ == '__main__':
	main()