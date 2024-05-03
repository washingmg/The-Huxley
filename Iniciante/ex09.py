

# QUESTÃO 326
# "Sequência lógica II"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


num1, num2 = map(int, input().split())

conta = 0
for num in range(1, num2 + 1):
    conta += 1
    if conta == num1 or num == num2:
        print(num)
        conta = 0
    else:
        print(num, end=" ")
