

# QUESTÃO 455
# "Vacinação"
# NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


idades_alunos = []

while True:
    idade = int(input())
    if idade == 100:
        break
    idades_alunos.append(idade)

vacinas_sarampo = 0
vacinas_hepatite = 0
vacinas_ambas = 0

for idade in idades_alunos:
    if 3 <= idade <= 6:
        vacinas_sarampo += 1
    if 5 <= idade <= 8:
        vacinas_hepatite += 1
    if 5 <= idade <= 6:  
        vacinas_ambas += 1

print(vacinas_sarampo)
print(vacinas_hepatite)
print(vacinas_ambas)
