import sys
import sucessor
import expande
from collections import deque

def busca_caminho(nodo_final, nodo_inicial):
	pilha_acoes = deque() # iremos empilhar as acoes já que a estaremos com a ordem reversa a priori
	v = nodo_final
	while v != nodo_inicial:
		pilha_acoes.append(v.acao)
		v = v.pai
	return pilha_acoes

def busca_dfs(nodo_inicial, custo_maximo_atual):
	objetivo = "12345678_"
	custo_maximo_absoluto = 100 #profundedade maxima tolerada
	explorados = set()
	fronteira = deque()
	fronteira.append(nodo_inicial)
	if custo_maximo_atual > custo_maximo_absoluto: #se a profundedade maxima atual é maior do que a profundedade maxima tolerada retorna -1 pois provavelmente não existe uma solução
		return -1
	while True:
		if not fronteira: # Se a fronteira esta vazia
			explorados = None
			return busca_dfs(nodo_inicial, custo_maximo_atual + 1) #executa a função novamente mas dessa vez com uma profundedade maxima maior
		v = fronteira.pop() #pop em vez de popleft para tratar a fronteira como pilha
		if v.estado == objetivo:
			return busca_caminho(v, nodo_inicial)
		if v not in explorados:
			explorados.add(v)
			estados_sucessores = sucessor.sucessor(v.estado)
			# Cada estado atingível a partir de v é acrescentado à fronteira caso a profundidade dos novos estados não exceda a profundidade máxima
			if (v.custo + 1) < custo_maximo_atual:
				for e in estados_sucessores:
					filho = expande.Nodo(e[1], v, e[0], v.custo + 1)
					fronteira.append(filho)

def main():
	#como eu não queria ter que modificar as classes que já existiam, usei o custo de cada estado como um sinônimo de profundidade, já que os novos estados sempre tem custo = custo do pai + 1
	estado_inicial = sys.argv[1]
	custo_inicial = 0
	pai = expande.Nodo(estado_inicial, 0, "", custo_inicial)
	caminho = busca_dfs(pai, 1)

	while caminho:
		print(caminho.pop(), end = " ")
	print()

if __name__ == '__main__':
	main()

