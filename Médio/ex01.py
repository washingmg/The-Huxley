

# QUESTÃO 2393
# "A FESTA DOS EXPANDEBLADES"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIA


minutos = int(input())  
quantidade_pessoas = max(1, minutos)

for _ in range(minutos):
    minutos *= 2

x = str(int(minutos / quantidade_pessoas))
if x != '0':  
    for i in range(0, len(x), 50):
        print(x[i:i+50])
else:
    print('1') 