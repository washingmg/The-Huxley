

# QUESTÃO 134
# "Botas perdidas"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


while True:
    n = int(input())
    
    if n == -1:
        break

    botas = {}

    for _ in range(n):
        tamanho, pe = input().split()
        if tamanho in botas:
            if pe in botas[tamanho]:
                botas[tamanho][pe] += 1 # acrescenta no dicionario no so seus respectivos valores
            else:
                botas[tamanho][pe] = 1
        else:
            botas[tamanho] = {pe: 1}
    
    pares = 0
    
    for pe in botas.values():
        if 'D' in pe and 'E' in pe:
            pares += min(pe['D'], pe['E'])
    
    print(pares)