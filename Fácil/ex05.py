

# QUESTÃO 1803
# "Vogais no texto"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


caracteres = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

string = input().lower()

for i in string:
    for _,u in caracteres.items():
        if i == _:
            caracteres[i] +=1
for i,u in caracteres.items():
    print(i, u)