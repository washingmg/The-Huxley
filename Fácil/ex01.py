

# QUESTÃO 3000
# "A GRANDE AMIGA"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


quantidade_pessoas = int(input())
dados = [input().split() for _ in range(quantidade_pessoas)]
idade = int(input())

amigos_com_idade = False
for nome, idade_amigo in dados:
    if int(idade_amigo) == idade:
        print(nome, end=' ')
        amigos_com_idade = True

if not amigos_com_idade:
    print('Eleven não tem amigos com essa idade.')
