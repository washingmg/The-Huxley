

# QUESTÃO 552
# "Algortimo de euclides"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

quantidade = int(input())
for i in range(quantidade):
    x, y = map(int, input().split())
    print(f'MDC({x},{y}) = {mdc(x, y)}')
