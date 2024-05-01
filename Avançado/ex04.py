

# QUESTÃO 2419
# "L1Q6 - Celulares Japoneses"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


dinheiro = float(input())

celulares = []

for i in range(3):
    linha = input().split()
    custo_beneficio = float(linha[1]) / float(linha[2])
    celular = (custo_beneficio, float(linha[1]), i + 1, linha[0], float(linha[2]))
    celulares.append(celular)

celulares.sort()

if dinheiro >= celulares[0][1]:
    print("Comprarei o celular", celulares[0][3])
else:
    print("O meu celular nem esta tao ruim assim")
