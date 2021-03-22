import board
from numpy import inf

def decisao_minimax(estado, cor_jogador, cor_oponente, profundidade):
    return valor_max(estado, cor_jogador, cor_oponente, -inf, inf, profundidade, True) #da o pontapé inicial
#---------------------------------------------------------------------------------------------------------------------
def valor_max(sting_tabuleiro, cor_jogador, cor_oponente, alfa, beta, profundidade, primeiria):
    #a string_tabuleiro se refere ao tabuleiro
    #as variaveis cor_jogador e cor_oponente se referem respectivamente as cores de cada jogador
    #alfa e beta são as variaveis de corte
    #profundidade se refere a profundidade maxima a ser pesquisada
    #primeira é um booleano para saber se é o primeiro max, se é, retorna a jogada a ser feita em vez do valor alfa
    tabuleiro = board.from_string(sting_tabuleiro) #cria o tabuleiro a partir da string recebida
    if profundidade == 0: #se chegou no maximo da profundidade
        return tabuleiro.piece_count[cor_jogador] #retorna o número de peças da cor do jogador contidas no tabuleiro
    jogadas_possiveis = tabuleiro.legal_moves(cor_jogador) #cria uma lista das jogadas possiveis para o jogador
    jogada_a_retornar = (-1, -1) #cria a variavel para guardar a jogada a ser feita
    for i in jogadas_possiveis: #verifica cada jogada possivel i
        tabuleiro = board.from_string(sting_tabuleiro) #recria o tabuleiro
        tabuleiro.process_move(i, cor_jogador) #faz a jogada i
        string_tabuleiro_novo = str(tabuleiro) #cria uma string do tabuleiro após a jogada i
        v = valor_min(string_tabuleiro_novo, cor_jogador, cor_oponente, alfa, beta, (profundidade - 1)) #faz o min do novo tabuleiro com frofundidade redusida
        #alfa = max(v, alfa)
        if v > alfa: #caso o valor v seja maior que o valor alfa
            alfa = v #alfa recebe v
            jogada_a_retornar = i #a jogada a ser retornada passa a ser i
        print("a jogada max ", i,  " retorna v = ", v, " e alfa = ", alfa, " e beta = ", beta, " e profundidade = ", profundidade) #print para testes
        if beta < alfa: #caso o beta seja menor que alfa
            if primeiria:
                return jogada_a_retornar #retorna a jogada caso esse seja o primeiro max
            else:
                return alfa #retorna o alfa caso esse não seja o primeiro max
    if primeiria:
        return jogada_a_retornar #retorna a ultima jogada feita
    else:
        return alfa #retorna alfa
#--------------------------------------------------------------------------------------------------------------------------
def valor_min(sting_tabuleiro, cor_jogador, cor_oponente, alfa, beta, profundidade):
    #a string_tabuleiro se refere ao tabuleiro
    #as variaveis cor_jogador e cor_oponente se referem respectivamente as cores de cada jogador
    #alfa e beta são as variaveis de corte
    #profundidade se refere a profundidade maxima a ser pesquisada
    tabuleiro = board.from_string(sting_tabuleiro) #cria o tabuleiro a partir da string recebida
    if profundidade == 0: #se chegou no maximo da profundidade
        return tabuleiro.piece_count[cor_jogador]  #retorna o número de peças da cor do jogador contidas no tabuleiro
    jogadas_possiveis = tabuleiro.legal_moves(cor_oponente) #cria uma lista das jogadas possiveis para o oponente
    for i in jogadas_possiveis: #verifica cada jogada possivel i
        tabuleiro = board.from_string(sting_tabuleiro) #recria o tabuleiro
        tabuleiro.process_move(i, cor_oponente)  #faz a jogada i
        string_tabuleiro_novo = str(tabuleiro) #cria uma string do tabuleiro após a jogada i
        v = valor_max(string_tabuleiro_novo, cor_jogador, cor_oponente, alfa, beta, (profundidade - 1), False) #faz o max do novo tabuleiro com frofundidade redusida
        beta = min(beta, v) #beta recebe o min entre beta e v
        print("a jogada min ", i,  " retorna v = ", v, " e alfa = ", alfa, " e beta = ", beta, " e profundidade = ", profundidade) #print para testes
        if alfa > beta:
            return beta #retorna beta caso o mesmo seja menor que alfa
    return beta #retorna beta

tabuleiro_string = "........\n........\n........\n...WB...\n...BW...\n........\n........\n........"

tabuleiro_obj = board.from_string(tabuleiro_string) #como construir um tabuleiro a partir de uma string
cor_jogador = tabuleiro_obj.WHITE
cor_oponente = tabuleiro_obj.BLACK
#tabuleiro_obj = board.Board()
#tabuleiro_obj.print_board()
#tabuleiro_obj.process_move((5, 3), tabuleiro_obj.WHITE) #como fazer uma jogada
#tabuleiro_obj.print_board()
#print(tabuleiro_obj.legal_moves(tabuleiro_obj.WHITE)) printa os movimentos permitidos as jogador branco

#valor_max(tabuleiro_string, tabuleiro_obj.WHITE, 0, 0, 0)
jogada = decisao_minimax(tabuleiro_string, cor_jogador, cor_oponente, 2) #teste pra ver se a função funciona
print(jogada)
