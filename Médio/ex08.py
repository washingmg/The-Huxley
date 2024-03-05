

# QUESTÃO 3857
# "ZECA NÃO QUER TRABALHAR"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO

def zeca(V, N, total_recebidos):
    total_recebidos.sort()
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if sum(total_recebidos[i:k+1]) == V:
                    return "Zeca nao vai ter que trabalhar!"
    return "Zeca vai ter que trabalhar."

V, N = map(int, input().split())
total_recebidos = list(map(int, input().split()))

print(zeca(V, N, total_recebidos))
