

# QUESTÃO 2457
# "A escadinha mágica"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE

quantidade = int(input())
for i in range(1, quantidade + 1):
    for j in range(1, i + 1):
        if i == j:
            print(i)
        else:
            print(j, end=' ')
