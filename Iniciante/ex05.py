

# QUESTÃO 2
# "3 Números em ordem crescente"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


num1 = int(input())
num2 = int(input())
num3 = int(input())

numeros_totais = [num1,num2,num3]
numeros_totais.sort()
for numero in numeros_totais:
    print(numero)