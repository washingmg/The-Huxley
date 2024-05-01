

# QUESTÃO 3553
# "COMPLETE O CÓDIGO COM A FUNÇÃO PEDIDA"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


# Escreva a funcao devolve_lista_numeros(x, y) abaixo:
def devolve_lista_numeros(x,y):
	x = [i for i in range(x, y +1)]
	return x

# PROGRAMA PRINCIPAL: nao altere o codigo a partir deste ponto
def programa_principal():
	a = int(input())
	b = int(input())
	resultado = devolve_lista_numeros(a, b)
	print(resultado)
programa_principal()