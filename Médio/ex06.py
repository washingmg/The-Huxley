

# QUESTÃO 9 28
# "CAMPO DE MINHOCAS"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


x, y = map(int, input().split())
all = []
for _ in range(x):
    linha = list(map(int, input().split()))
    all.append(linha)

total = 0
for i in range(x):
    soma_linha = sum(all[i])
    total = max(total, soma_linha)
    
    for j in range(y):
        soma_coluna = sum(all[k][j] for k in range(x))
        total = max(total, soma_coluna)

print(total)