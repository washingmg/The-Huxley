

# QUESTÃO 154
# "Auto-estrada"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


inteiro = input()
string = input()

caracteres = {'P':2, 'A':1, 'C':2, 'D':0}

total = 0
for i in string:
    for _,u in caracteres.items():
        if i == _:
            total += u
print(total)