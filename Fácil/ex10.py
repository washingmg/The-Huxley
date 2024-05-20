

# QUESTÃO 1183
# "Anagrama de uma frase"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


frase1 = input().upper()
frase2 = input().upper()

prejudica = '!., ?'

sequencia1 = []
sequencia2 = []

for _ in frase1:
    if _ not in prejudica:
        sequencia1.append(_)

for _ in frase2:
    if _ not in prejudica:
        sequencia2.append(_)

sequencia1.sort()
sequencia2.sort()
print(sequencia1)

if sequencia1 == sequencia2:
    print("True")
else:
    print("False")
