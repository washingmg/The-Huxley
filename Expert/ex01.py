

# QUESTÃO 640
# "Copa do Mundo (Maratona)"
# NÍVEL DE ACORDO COM O THE HUXLEY: EXPERT

def calcular_empates(T, N, times):
    total_pontos = sum(int(pontos) for _, pontos in times)
    empates = total_pontos - 3 * N
    return empates

while True:
    T, N = map(int, input().split())
    if T == 0:
        break
    times = [input().split() for _ in range(T)]
    empates = calcular_empates(T, N, times)
    print(abs(empates))
