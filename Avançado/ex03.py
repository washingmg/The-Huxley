

# QUESTÃO 2498
# "Ticket da sorte"
# NÍVEL DE ACORDO COM O THE HUXLEY: AVANÇADO


num = input()
tamanho = len(num)

soma_ate_metade = 0
soma_da_metade_ate_fim = 0

metdade = tamanho / 2

for i in range(int(metdade)):
    soma_ate_metade += int(num[i])

for i in range(int(metdade), tamanho):
    soma_da_metade_ate_fim += int(num[i])

if soma_ate_metade == soma_da_metade_ate_fim:
    print('True')
else:
    print('False')