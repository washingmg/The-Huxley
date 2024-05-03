

# QUESTÃO 244
# "Contar um caracter na string"
# NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


frase = input()
letra = input()

cont = 0
for _ in frase:
    if letra == _:
        cont +=1
print(cont)