

# QUESTÃO 817
# "CHUVA (OBI)"
# NÍVEL DE ACORDO COM O THE HUXLEY: AVANÇADO


def cobertoAgua(N, alturas):
    max_altura_esquerda, agua_coberta = alturas[0], 0

    for i in range(1, N):
        max_altura_esquerda = max(max_altura_esquerda, alturas[i])
        if min(max_altura_esquerda, max(alturas[i+1:])) > alturas[i]:
            agua_coberta += 1

    return agua_coberta


N = int(input())
alturas = [int(input()) for _ in range(N)]

print(cobertoAgua(N, alturas))
