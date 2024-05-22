

# QUESTÃO 776
# "Moda de conjunto de inteiros"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


valores = input().split()

valores_int = [int(valor) for valor in valores]

frequencias = {}
for valor in valores_int:
    if valor in frequencias:
        frequencias[valor] += 1
    else:
        frequencias[valor] = 1

maior_frequencia = 0
moda = None

for valor, frequencia in frequencias.items():
    if frequencia > maior_frequencia:
        moda = valor
        maior_frequencia = frequencia

print("Moda =", moda)