# QUESTÃO 3271
# "TODOS OS ÍNDICES DE OCORRÊNCIA"
# NÍVEL DE ACORDO COM O THE HUXLEY: MÉDIO


# Escreva a funcao todos_os_indices(seq, x) abaixo:
def todos_os_indices(seq, x):
    lista = [_ for _ in seq]
    indices = []
    for i, _ in enumerate(lista):
        if seq[i] == x:
            indices.append(i)
    return indices

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
sequencia = eval(input())
valor = eval(input())
resultado = todos_os_indices(sequencia, valor)
if isinstance(resultado, list):
    if len(resultado) > 0:
        for item in resultado:
            print(item)
    else:
        print('lista vazia')
else:
    print('Erro. Voce deve devolver uma lista')