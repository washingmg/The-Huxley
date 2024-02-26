

# QUESTÃO 2069
# "FREQUÊNCIA DE NÚMERO"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


quantidade_numeros, numero = input().split()
print(sum(1 for _ in range(int(quantidade_numeros)) if input() == numero))
