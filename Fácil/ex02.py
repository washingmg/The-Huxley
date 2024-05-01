

# QUESTÃO 3250
# "FUNÇÕES:TESTE A QUANTIDADE DE DIVISORES DE N"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


# Escreva a funcao checa_quantidade_divisores(n, qtd) na sequencia:
def checa_quantidade_divisores(n,qtd):
	divisores = 0
	for _ in range(1,n+1):
		if (n % _) == 0:
			divisores +=1
	if divisores == qtd:
		return True
	else:
		return False

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
n = int(input())
qtd = int(input())
if checa_quantidade_divisores(n, qtd): # se a funcao devolve True, entao...
	print(n, "possui", qtd, "divisores")
else:
	print(n, "nao possui", qtd, "divisores")