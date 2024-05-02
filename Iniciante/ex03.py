

# QUESTÃO 3346
# "LISTA PYTHON - SOMATÓRIO"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE

numeros = []
terminou = False
while not terminou:
    entrada = int(input())
    if entrada == -1:
        terminou = True
    else:
        numeros.append(entrada)
i = 0
for _ in numeros:
    i+=1
print(f'{(sum(numeros)/ i):.2f}')