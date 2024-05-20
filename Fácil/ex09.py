

# QUESTÃO 250
# "Índices de um caracter na string"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


frase = input()
letra = input()

cont = -1
tamanho = len(frase)
for _ in frase:
    cont +=1
    if letra == _:
        print(cont)
print('-1')