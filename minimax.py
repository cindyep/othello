class Nodo:
	def __init__(self, estado, pai, acao, alfa, beta):
		self.estado = estado
		self.pai = pai
		self.acao = acao
		self.alfa_beta = (alfa, beta)
	def imprimeNodo(self):
		print("(" + self.acao + "," + self.estado + "," + str(self.alfa_beta) + "," + self.pai.estado + ")", end = "")

# Função: decisão(estado)
# Entrada: estado
# Saída: ação cujo sucessor tem valor v
def decisao(estado):
	v = valor_max(estado);

# Função: valor_max(estado)
# Entradas: estado, valor alfa, valor beta
# Saída: valor máximo
def valor_max(estado, alfa, beta):

# Função: valor_min(estado)
# Entradas: estado, valor alfa, valor beta
# Saída: valor mínimo
def valor_max(estado, alfa, beta):