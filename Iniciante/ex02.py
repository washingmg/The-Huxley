

# QUESTÃO 3919
# "20 NÚMEROS DO TIO WILLY"
# NÍVEL DE ACORDO COM O THE HUXLEY: INCIANTE


x = [int(input()) for _ in range(21)]
e = 0
for i in x[1:]:
    if x[0] == i:
        n = i
        e+= 1
    if i == -1:
        break
print(f'{n} aparece {e} vezes')