from othello import imprime_tabuleiro

class Nodo:
	def __init__(self, estado, pai, acao, alfa, beta):
		self.estado = estado # tabuleiro
		self.pai = pai
		self.acao = acao # onde coloca sua peça
		self.alfa_beta = (alfa, beta)

	def imprimeNodo(self):
		print("(" + str(self.acao) + ", " + str(self.alfa_beta) + ")")
		print("estado:")
		imprime_tabuleiro(self.estado)

# Função: decisão(estado)
# Entrada: estado
# Saída: ação cujo sucessor tem valor v
#def decisao(estado):
#	v = valor_max(estado);

# Função: valor_max(estado)
# Entradas: estado, valor alfa, valor beta
# Saída: valor máximo
#def valor_max(estado, alfa, beta):

# Função: valor_min(estado)
# Entradas: estado, valor alfa, valor beta
# Saída: valor mínimo
#def valor_max(estado, alfa, beta):

# Conta peças no tabuleiro do jogador especificado na chamada
def conta_pecas(jogador, tabuleiro):
	pecas = 0
	for y in range(0, 7):
		for x in range(0, 7):
			if(tabuleiro[(x, y)] == jogador):
				pecas += 1
	return pecas

