

# QUESTÃO 2421
# "L1Q7 - Moedas infinitas"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


moedas = int(input())
m500, m100, m50, m10, m5, m1 = 0, 0, 0, 0, 0, 0

m500 = moedas // 500
moedas %= 500
m100 = moedas // 100
moedas %= 100
m50 = moedas // 50
moedas %= 50
m10 = moedas // 10
moedas %= 10
m5 = moedas // 5
moedas %= 5
m1 = moedas // 1

print(f"{m500} moedas de 500.")
print(f'{m100} moedas de 100.')
print(f'{m50} moedas de 50.')
print(f'{m10} moedas de 10.')
print(f'{m5} moedas de 5.')
print(f'{m1} moedas de 1.')
