

# QUESTÃO 1009
# "PALÍNDROMO"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


def palindromo(entrada):
    if entrada == entrada[::-1]:
        print('S')
    else:
        print('N')
palindromo(input())