

# QUESTÃO 201
# "Zerinho ou um"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


def determina_vencedor(A, B, C):
    if A != B and A != C:
        return 'A'
    elif B != A and B != C:
        return 'B'
    elif C != A and C != B:
        return 'C'
    else:
        return '*'


A = input()
B = input()
C = input()

vencedor = determina_vencedor(A, B, C)

print(vencedor)
